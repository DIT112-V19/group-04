#ifndef USEDPINS_H
#define USEDPINS_H

// left motor pins
const int BRUSHED_LEFT_FORWARD_PIN = 8;
const int BRUSHED_LEFT_BACKWARD_PIN = 10;
const int BRUSHED_LEFT_ENABLE_PIN = 9;

// right motor pins
const int BRUSHED_RIGHT_FORWARD_PIN = 12;
const int BRUSHED_RIGHT_BACKWARD_PIN = 13;
const int BRUSHED_RIGHT_ENABLE_PIN = 11;

// odometer pins
const int ODOM_LEFT_PIN = 2;
const int ODOM_RIGHT_PIN = 3;

// ultra sound pins
const int US_TRIGGER_PIN = 5;
const int US_ECHO_PIN = 4;

// bluetooth pins
#define BLUETOOTH     Serial3

#endif
