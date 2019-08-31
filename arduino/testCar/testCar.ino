#include <Smartcar.h>
#include "pathfinder.h"
#include "constants.h"
#include "usedpins.h"

// classes to control the car
BrushedMotor leftMotor(BRUSHED_LEFT_FORWARD_PIN, BRUSHED_LEFT_BACKWARD_PIN, BRUSHED_LEFT_ENABLE_PIN);
BrushedMotor rightMotor(BRUSHED_RIGHT_FORWARD_PIN, BRUSHED_RIGHT_BACKWARD_PIN, BRUSHED_RIGHT_ENABLE_PIN);
DifferentialControl control(leftMotor, rightMotor);

// sensors on the car
DirectionlessOdometer leftOdometer(200), rightOdometer(200);    // two odometers
GY50 gyroscope(GYROSCOPE_OFFSET);     // gyroscope
SR04 frontUltrasound(US_TRIGGER_PIN, US_ECHO_PIN, US_MAX_DISTANCE);   // ultra sound distance sensor

// HeadingCar and PathFinder derived from it
HeadingCar car(control, gyroscope);
PathFinder pathy(car, &Serial3, &leftOdometer, &rightOdometer, &frontUltrasound, Point(30, 2));

// variable to store the time at program start in ms
unsigned long startTime;


/**
 * Set up the odometers and initialise the car before starting the program
 */
void setup() {
  // set up interrupts for the odometers (doesn't work from the PathFinder init)
  leftOdometer.attach(ODOM_LEFT_PIN, []() {
    leftOdometer.update();
  });
  rightOdometer.attach(ODOM_RIGHT_PIN, []() {
    rightOdometer.update();
  });

  // initialise the PathFinder
  pathy.init();
  
  startTime = millis();
}


/**
 * This function is continously looping the program implemented for the car.
 * 
 * It is important for all used functions to implement non-blocking behaviour. 
 * This ensures that the single thread used for the application can handle all
 * situations immediately.
 */
void loop() {  
  pathy.update();   // update everything on the pathfinder -- this controls what the car does
  unsigned long now = millis();   // get the current time in ms
  
  // print only every PRINT_PERIOD
  if (now - startTime > PRINT_PERIOD) {
    int heading = pathy.getHeading();
    pathy.publishPos();
    startTime = startTime + PRINT_PERIOD;     // prevent the printing time from drifting (would happen if it was set to now instead)
  }
}
