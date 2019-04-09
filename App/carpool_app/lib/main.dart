import 'package:flutter/material.dart';
import 'dart:io';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Carpooloza',
      theme: ThemeData(

        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Carpooloza'),
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

  Future sendInstructions(String directions) async {
  var server = await HttpServer.bind(
    InternetAddress.loopbackIPv4,
    3000,
  );
  print('Listening on localhost:${server.port}');

  await for (HttpRequest request in server) {
    request.response
      ..write(directions)
      ..close();
  }
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
            FlatButton(
              child: Container(
                child: Center(
                  child: Text("GO", style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 40),),
                ),
                height: 100,
                width: 300,
                decoration: BoxDecoration(
                  color: Colors.blue,
                  borderRadius: BorderRadius.all(Radius.circular(50))
                ),
              ),
              onPressed: () {
                // send request
                sendInstructions('Forward');
              },
            )
          ],
        ),
      ),
    );
  }
}
