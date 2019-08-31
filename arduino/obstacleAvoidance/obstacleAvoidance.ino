// very basic obstacle avoidance
// stop the car when an obstacle gets to close to the front sensor

#include <Smartcar.h>
#include "constants.h"
#include <SoftwareSerial.h>

// constants within this file (might need to be replaced with variables at some point)
const int SPEED = 25;
const int STOP_SPEED = 0;
const int SAFETY_DIST = 25; // not yet intended as the global standard - move to constants.h if it becomes that

// instantiate the front ultra sound sensor
SR04 front(US_TRIGGER_PIN, US_ECHO_PIN, US_MAX_DISTANCE);

// instantiate SimpleCar using differential control
BrushedMotor leftMotor(BRUSHED_LEFT_FORWARD_PIN, BRUSHED_LEFT_BACKWARD_PIN, BRUSHED_LEFT_ENABLE_PIN );
BrushedMotor rightMotor(BRUSHED_RIGHT_FORWARD_PIN, BRUSHED_RIGHT_BACKWARD_PIN, BRUSHED_RIGHT_ENABLE_PIN);
DifferentialControl control(leftMotor, rightMotor);
SimpleCar car(control);

char c;
int speed = STOP_SPEED;

String buffer = "";

HardwareSerial connection = Serial1;

void setup() {
  // initialize serial communication
  connection.begin(BAUD_RATE);
}

void readCommand(String command) {
  if (command == "MOVE") {
    car.setSpeed(SPEED);
  } else if (command == "STOP") {
    car.setSpeed(STOP_SPEED);
  }
}


void readSerial() {
  while (connection.available() > 0) {
    char received = connection.read();
    if (received == '\n') {
      readCommand(buffer);
      buffer = "";
    } else {
      buffer += received;  
    }      
  }  
}

void loop() {
  readSerial();
  
  int dist = front.getDistance();   // read front distance
  
  // stop car if necessary to avoid collision
  if (dist < SAFETY_DIST && dist > 0) {
    speed = STOP_SPEED;
    car.setSpeed(speed);
  }
  /*else if (connection.available()) {
    c = connection.read();
    // set initial speed of the car
    if (c == 'M') {
      speed = (speed == STOP_SPEED) ? SPEED : STOP_SPEED;    
      car.setSpeed(speed); 
      //Serial1.println(speed);        
    }
  }*/
}
