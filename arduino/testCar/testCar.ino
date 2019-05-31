#include <Smartcar.h>
#include "pathfinder.h"
#include "constants.h"
#include "usedpins.h"

const int carSpeed = 50; // 50% of the max speed

// classes to control the car
BrushedMotor leftMotor(BRUSHED_LEFT_FORWARD_PIN, BRUSHED_LEFT_BACKWARD_PIN, BRUSHED_LEFT_ENABLE_PIN);
BrushedMotor rightMotor(BRUSHED_RIGHT_FORWARD_PIN, BRUSHED_RIGHT_BACKWARD_PIN, BRUSHED_RIGHT_ENABLE_PIN);
DifferentialControl control(leftMotor, rightMotor);

// sensors on the car
DirectionlessOdometer leftOdometer(200), rightOdometer(200);
GY50 gyroscope(GYROSCOPE_OFFSET);

HeadingCar car(control, gyroscope);
PathFinder pathy(car, &Serial3, &leftOdometer, &rightOdometer, Point(30, 2));

unsigned long startTime;

void setup() {
  // set up interrupts for the odometers
  leftOdometer.attach(ODOM_LEFT_PIN, []() {
    leftOdometer.update();
  });
  rightOdometer.attach(ODOM_RIGHT_PIN, []() {
    rightOdometer.update();
  });
  
  // put your setup code here, to run once:
  startTime = millis();  // variable holding the time program start in ms
  pathy.init();
  // BLUETOOTH.begin(BAUD_RATE);
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
  if (now - startTime > PRINT_PERIOD) {
    int heading = pathy.getHeading();
    pathy.publishPos();
    startTime = startTime + PRINT_PERIOD;     // prevent the printing time from drifting (would happen if it was set to now instead)
  }
}
