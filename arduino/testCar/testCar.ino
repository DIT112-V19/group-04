#include <Smartcar.h>
#include "pathfinder.h"
#include "constants.h"
#include "usedpins.h"

const int carSpeed = 50; // 50% of the max speed

BrushedMotor leftMotor(BRUSHED_LEFT_FORWARD_PIN, BRUSHED_LEFT_BACKWARD_PIN, BRUSHED_LEFT_ENABLE_PIN);
BrushedMotor rightMotor(BRUSHED_RIGHT_FORWARD_PIN, BRUSHED_RIGHT_BACKWARD_PIN, BRUSHED_RIGHT_ENABLE_PIN);
DifferentialControl control(leftMotor, rightMotor);

GY50 gyroscope(GYROSCOPE_OFFSET);

HeadingCar car(control, gyroscope);
Bluetooth blue(Serial3);
PathFinder pathy(car, blue, DEFAULT_X, DEFAULT_Y);

unsigned long start_time;

void setup() {
  // put your setup code here, to run once:
  //Serial.begin(9600);
  //Serial.println(pathy.getHeading(), DEC);
  start_time = millis();  // variable holding the time program start in ms
  pathy.init();
  Serial3.begin(BAUD_RATE);
}


/**
 * This function is continously looping the program implemented for the car.
 * 
 * It is important for all used functions to implement non-blocking behaviour. 
 * This ensures that the single thread used for the application can handle all
 * situations immediately.
 */
void loop() {
  // put your main code here, to run repeatedly:
  
  unsigned long now = millis();   // get the current time in ms
  pathy.update();   // update everything on the pathfinder -- this controls what the car does

  // print only every PRINT_PERIOD
  if (now - start_time > PRINT_PERIOD) {
    int heading = pathy.getHeading();
    Serial3.println(heading, DEC);
    start_time = start_time + PRINT_PERIOD;     // prevent the printing time from drifting (would happen if it was set to now instead)
  }
}
