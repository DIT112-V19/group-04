#ifndef PATHCAR_H
#define PATHCAR_H

#include <Smartcar.h>
#include "bluetooth.h"
#include "constants.h"
#include "usedpins.h"
#include <stdlib.h>

static const int DEG_IN_CIRCLE = 360;
static const int ANGLE_TOLERANCE = 5;

static const double DEFAULT_X = 0.0;
static const double DEFAULT_Y = 0.0;
static const double DEFAULT_THETA = 0.0;

class PathFinder {
private:
  HeadingCar mCar;
  Bluetooth mConnection;
  DirectionlessOdometer mLeftOdo;
  DirectionlessOdometer mRightOdo;
  
  double mX;
  double mY;
  int mHeading;

  bool mTurn;
  int mTargetHeading;
  
  bool mDrive;
  double mTargetDistance; 


public:
  PathFinder(const HeadingCar& car, const Bluetooth& blue, const DirectionlessOdometer& leftOdo, const DirectionlessOdometer& rightOdo, double x, double y);
  PathFinder(const HeadingCar car, const Bluetooth blue, const DirectionlessOdometer& leftOdo, const DirectionlessOdometer rightOdo) : PathFinder(car, blue, leftOdo, rightOdo, DEFAULT_X, DEFAULT_Y){};


  double getX() {return mX;}
  double getY() {return mY;}
  int getHeading() {return mHeading;};

  void init();
  void update();
  HardwareSerial getConnection() {return mConnection.getConnection();}
  
  void rotateOnSpot(int targetDegrees, int speed);
  void rotateToHeading(int targetHeading, int speed);

  void moveForward(int distance, int speed);
};

int trimHeading(int heading);

#endif
