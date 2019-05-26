import 'dart:convert';
import 'dart:math';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

import 'models.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Carpool App',
      color: blueColor,
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

  String url = "http://127.0.0.1:5000/api/";  //"http://carpool.serveo.net/api";

  double posxDestination = 100.0;
  double posyDestination = 100.0;
  double posxCurrent = 100.0;
  double posyCurrent = 100.0;

  Map locOrDest = new Map();

  void onTapDown(BuildContext context, TapDownDetails details, int locationOrDestination) {
    print('${details.globalPosition}');
    final RenderBox box = context.findRenderObject();
    final Offset localOffset = box.globalToLocal(details.globalPosition);
    setState(() {
      if (locationOrDestination == 1) {
        posxCurrent = localOffset.dx;
        posyCurrent = localOffset.dy;
      } else {
        posxDestination = localOffset.dx;
        posyDestination = localOffset.dy;
      }
      locOrDest = ({
        1: [posxCurrent, posyCurrent],
        2: [posxDestination, posyDestination],
      });
    });
  }

  Map<String, String> headers = {
    "Cookie": "id=kalle",
    "Content-type" : "application/json"
  };

  void sendInfo(List<double> current, List<double> destination) async {
    final response = await http.post('$url' + 'pickup',
      body: json.encode(locationToJson(current, destination)),
      headers: headers,
    );
    print(response.body);
  }


Map<String, dynamic> locationToJson(List<double> x, List<double> y) => {
            "location" : x,
            "destination" : y,
    };

  Icon pin = new Icon(Icons.pin_drop);
  bool isLocation = true;
  bool locationHasBeenSet = false;
  bool destinationHasBeenSet = false;

  MarkerLayoutDelegate delegate = MarkerLayoutDelegate(relayout: CallableNotifier());
  Widget getGestureDetector() {
    return new Container(
      height: 210,
      width: 400,
      color: Colors.white,
      child: GestureDetector(
        // onPanUpdate: (p) {
        //   delegate.position += p.delta;
        // },
      onTapDown: (TapDownDetails details) {
        int destOrLoc = 1;
        if (isLocation) {
          destOrLoc = 1;
          locationHasBeenSet = true;
        } else {
          destOrLoc = 2;
          destinationHasBeenSet = true;
        }
        onTapDown(context, details, destOrLoc);
      },
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
          child: pin,           
          left: posxCurrent,
          top: posyCurrent,
        )
      ]),
    ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title, style: buttonTextStyle,),
        backgroundColor: blueColor,
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Container(
              margin: EdgeInsets.only(bottom: 20),
              child: Column(
                children: <Widget>[
                              RaisedButton(
              color: blueColor,
              child: Container(
                width: 140,
                child: Center(
                  child: Text("Set Your Location", style: buttonTextStyle,),
                ),
              ),
              onPressed: () {
                isLocation = true;
              },
            ),
            RaisedButton(
              color: blueColor,
              child: Container(
                width: 140,
                child: Center(
                  child: Text("Set Destination", style: buttonTextStyle),
                ),
              ),
              onPressed: () {
                isLocation = false;
              },
            ),
                ],
              ),
            ),
            getGestureDetector(),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          // send info
          if (locationHasBeenSet && destinationHasBeenSet) {
            sendInfo(locOrDest[1], locOrDest[2]);
          }
        },
        backgroundColor: blueColor,
        tooltip: 'Increment',
        child: Icon(Icons.drive_eta),
      ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}
class CallableNotifier extends ChangeNotifier {
  void notify() {
    this.notifyListeners();
  }
}
class MarkerLayoutDelegate extends SingleChildLayoutDelegate with ChangeNotifier {
  Offset position;

  CallableNotifier _notifier;

  MarkerLayoutDelegate({CallableNotifier relayout});

  @override
  BoxConstraints getConstraintsForChild(BoxConstraints constraints) {
    return constraints.loosen();
  }

  @override
  Offset getPositionForChild(Size size, Size childSize) {
    return Offset(min(position.dx, size.width - childSize.width), min(position.dy, size.height - childSize.height));
  }

  @override
  bool shouldRelayout(MarkerLayoutDelegate oldDelegate) {
    return position != oldDelegate.position;
  }
}
