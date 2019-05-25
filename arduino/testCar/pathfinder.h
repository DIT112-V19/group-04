#ifndef PATHCAR_H
#define PATHCAR_H

#include <Smartcar.h>
#include "bluetooth.h"
#include "constants.h"
#include "usedpins.h"
#include "point.h"
#include <stdlib.h>

static const int DEG_IN_CIRCLE = 360;
static const int ANGLE_TOLERANCE = 5;

static const double DEFAULT_THETA = 0.0;

class PathFinder {
private:
  HeadingCar mCar;
  Bluetooth *mConnection;
  DirectionlessOdometer *mLeftOdo;
  DirectionlessOdometer *mRightOdo;

  Point mPos;
  double mX;
  double mY;
  int mHeading;
  int mDistance;

  bool mTurn;
  int mTargetHeading;
  
  bool mDrive;
  int mTargetDistance; 

  Point path[64];


public:
  PathFinder(const HeadingCar& car, const Bluetooth *blue, const DirectionlessOdometer *leftOdo, const DirectionlessOdometer *rightOdo, Point pos);
  PathFinder(const HeadingCar& car, const Bluetooth *blue, const DirectionlessOdometer *leftOdo, const DirectionlessOdometer *rightOdo) : PathFinder(car, blue, leftOdo, rightOdo, Point(DEFAULT_X, DEFAULT_Y)){};


  Point getPos() {return mPos;}
  int getHeading() {return mHeading;};
  int getDistance() {return mDistance;};

  void init();
  void update();
  HardwareSerial getConnection() {return mConnection->getConnection();}

  void println(String text);
  
  void rotateOnSpot(int targetDegrees, int speed);
  void rotateToHeading(int targetHeading, int speed);

  void moveForward(int distance, int speed);
};

int trimHeading(int heading);

#endif
