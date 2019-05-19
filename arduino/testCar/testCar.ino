#include <Smartcar.h>
#include "pathfinder.h"

const int carSpeed = 50; //80% of the max speed
const int GYROSCOPE_OFFSET = 37;

BrushedMotor leftMotor(8, 10, 9);
BrushedMotor rightMotor(12, 13, 11);
DifferentialControl control(leftMotor, rightMotor);

GY50 gyroscope(GYROSCOPE_OFFSET);

HeadingCar car(control, gyroscope);
Bluetooth blue(Serial3);
PathFinder pathy(car, blue, 0.0, 0.0);
HardwareSerial ser = Serial3;

unsigned long start_time;

void setup() {
  // put your setup code here, to run once:
  //Serial.begin(9600);
  //Serial.println(pathy.getHeading(), DEC);
  pathy.init();
  start_time = millis();
  ser.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  unsigned long now = millis();   // get the current time in ms
  pathy.update();   // update everything on the pathfinder

  // print only every 1000 milli seconds
  if (now - start_time > 1000) {
    int heading = pathy.getHeading();
    Serial3.println(heading, DEC);
    start_time = now;  
  }
}
