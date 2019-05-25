#ifndef PATHCAR_H
#define PATHCAR_H

#include <Smartcar.h>
#include "bluetooth.h"
#include "constants.h"
#include "usedpins.h"
#include "point.h"
#include <stdlib.h>
#include <math.h>

static const int DEG_IN_CIRCLE = 360;
static const int ANGLE_TOLERANCE = 5;

static const double DEFAULT_THETA = 0.0;

static const int MAX_PATH_LENGTH = 64;

class PathFinder {
private:
  HeadingCar mCar;
  Bluetooth *mConnection;
  DirectionlessOdometer *mLeftOdo;
  DirectionlessOdometer *mRightOdo;

  Point mPos;
  int mSpeed;
  int mHeading;
  int mDistance;

  bool mTurn;
  int mTargetHeading;
  
  bool mDrive;
  int mTargetDistance; 

  Point *mPath[MAX_PATH_LENGTH];
  int mReadPosition;
  int mWritePosition;

public:
  PathFinder(const HeadingCar& car, const Bluetooth *blue, const DirectionlessOdometer *leftOdo, const DirectionlessOdometer *rightOdo, Point pos, int speed=SPEED);
  PathFinder(const HeadingCar& car, const Bluetooth *blue, const DirectionlessOdometer *leftOdo, const DirectionlessOdometer *rightOdo, int speed=SPEED) : 
                PathFinder(car, blue, leftOdo, rightOdo, Point(DEFAULT_X, DEFAULT_Y), speed){};


  Point getPos() {return mPos;}
  int getHeading() {return mHeading;};
  int getDistance() {return mDistance;};
  int getSpeed() {return mSpeed;};
  void setSpeed(int speed) {mSpeed = speed;};

  void init();
  void update();
  HardwareSerial getConnection() {return mConnection->getConnection();}

  void println(String text);
  
  void rotateOnSpot(int targetDegrees);
  void rotateToHeading(int targetHeading);

  void moveForward(int distance);
  void goTo(Point destination);

  void clearPath();  
  void addPoint(const Point *point);
};

int trimHeading(int heading);

#endif
