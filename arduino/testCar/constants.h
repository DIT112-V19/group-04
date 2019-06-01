#ifndef CONSTANTS_H
#define CONSTANTS_H

//#define DEBUG     // switch for debugging - comment out for the final product

// ultra sound settings
const int US_MAX_DISTANCE = 100;
const int US_SAFETY_DIST = 25;

// other settings
const int BAUD_RATE = 9600;       // baud rate for serial communication
const int GYROSCOPE_OFFSET = 37;  // gyroscope calibration result
const int SPEED = 25;             // speed the car is using when driving
const int STOP_SPEED = 0;         // speed to stop the car
const int PRINT_PERIOD = 1000;    // in ms
static const int DEG_IN_CIRCLE = 360;   // amount of degrees in a full circle

// command syntax
static const char CLEAR_CMD[] = "F**K";
static const char APPENDER = '<';
static const char SEPARATOR = ',';
static const char CLOSER = '>';

#endif
