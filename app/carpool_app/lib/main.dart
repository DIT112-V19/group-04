import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Carpool App',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Carpool App'),
    );
  }
}



class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  String url = "https://carpool.serveo.net";

  double posx = 100.0;
  double posy = 100.0;

  void onTapDown(BuildContext context, TapDownDetails details) {
    print('${details.globalPosition}');
    final RenderBox box = context.findRenderObject();
    final Offset localOffset = box.globalToLocal(details.globalPosition);
    setState(() {
      posx = localOffset.dx;
      posy = localOffset.dy;
    });
  }

  void sendInfo(double x, double y) async {
    final response = await http.post('$url/',
      body: locationToJson(x, y).toString()
    );
    print(response.body);
  }


Map<String, double> locationToJson(double x, double y) => {
            'x' : x,
            'y' : y,
    };



  Widget getGestureDetector() {
    return new Container(
      height: 300,
      width: 400,
      color: Colors.white,
      child: GestureDetector(
      onTapDown: (TapDownDetails details) => onTapDown(context, details),
      child: new Stack(fit: StackFit.expand, children: <Widget>[
        // Hack to expand stack to fill all the space. There must be a better
        // way to do it.
        Container(
          decoration: BoxDecoration(
            image: DecorationImage(
              image: AssetImage('lib/assets/map.png'),
              ),
          ),
        ),
        new Positioned(
          child: new Text(''),
          left: posx,
          top: posy,
        )
      ]),
    ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            getGestureDetector(),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          // send info
          print(posx);
          print(posy);
          sendInfo(posx, posy);
        },
        tooltip: 'Increment',
        child: Icon(Icons.drive_eta),
      ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}
