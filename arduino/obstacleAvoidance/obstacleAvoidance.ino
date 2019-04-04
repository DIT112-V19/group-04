// very basic obstacle avoidance
// stop the car when an obstacle gets to close to the front sensor

#include <Smartcar.h>
#include "constants.h"

// constants within this file (might need to be replaced with variables at some point)
const int SPEED = 100;
const int STOP_SPEED = 0;
const int SAFETY_DIST = 25; // not yet intended as the global standard - move to constants.h if it becomes that

// instantiate the front ultra sound sensor
SR04 front(US_TRIGGER_PIN, US_ECHO_PIN, US_MAX_DISTANCE);

// instantiate SimpleCar using differential control
BrushedMotor leftMotor(BRUSHED_LEFT_FORWARD_PIN, BRUSHED_LEFT_BACKWARD_PIN, BRUSHED_LEFT_ENABLE_PIN );
BrushedMotor rightMotor(BRUSHED_RIGHT_FORWARD_PIN, BRUSHED_RIGHT_BACKWARD_PIN, BRUSHED_RIGHT_ENABLE_PIN);
DifferentialControl control(leftMotor, rightMotor);
SimpleCar car(control);


void setup() {
  // initialize serial communication
  Serial.begin(BAUD_RATE);

  // set initial speed of the car
  car.setSpeed(SPEED);
}

void loop() {
  int dist = front.getDistance();   // read front distance
  
  // stop car if necessary to avoid collision
  if (dist < SAFETY_DIST && dist > 0) {
    car.setSpeed(STOP_SPEED);
  }
}
