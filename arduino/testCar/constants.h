#ifndef CONSTANTS_H
#define CONSTANTS_H
#include "usedpins.h"

#define DEBUG     // switch for debugging - comment out for the final product

// ultra sound settings
const int US_MAX_DISTANCE = 100;

// serial communication settings
const int BAUD_RATE = 9600;

// gyroscope calibration result
const int GYROSCOPE_OFFSET = 37;

// speed
const int SPEED = 25;


// printing 
const int PRINT_PERIOD = 1000; // in ms

#endif
