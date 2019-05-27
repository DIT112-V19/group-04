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

  Point mPos = Point(0, 0);
  Point mPrev = Point(0, 0);
  int mSpeed;
  int mHeading = 0;
  int mDistance = 0;

  bool mTurn = false;
  int mTargetHeading = 0;
  
  bool mDrive = false;
  int mTargetDistance = 0; 

  Point mPath[MAX_PATH_LENGTH];
  int mReadPosition = 0;
  int mWritePosition = 0;

public:
  PathFinder(const HeadingCar& car, const Bluetooth *blue, const DirectionlessOdometer *leftOdo, const DirectionlessOdometer *rightOdo, Point pos, int speed=SPEED);
  PathFinder(const HeadingCar& car, const Bluetooth *blue, const DirectionlessOdometer *leftOdo, const DirectionlessOdometer *rightOdo, int speed=SPEED) : 
                PathFinder(car, blue, leftOdo, rightOdo, Point(DEFAULT_X, DEFAULT_Y), speed){};


  Point getPos() {return mPos;}
  int getHeading() {return mHeading;};
  int getDistance() {return mDistance;};
  int getTargetDistance() {return mTargetDistance;};
  void setTargetDistance(int dist) {mTargetDistance = dist;};
  int getSpeed() {return mSpeed;};
  void setSpeed(int speed) {mSpeed = speed;};
  

  void init();
  void update();
  void updatePosition();
  HardwareSerial getConnection() {return mConnection->getConnection();}

  void println(String text);
  
  void rotateOnSpot(int targetDegrees);
  void rotateToHeading(int targetHeading);

  void moveForward(int distance);
  void goToPoint(Point destination);

  void clearPath();  
  void addPoint(const Point point);
  void setNextGoal();
};

int trimHeading(int heading);

#endif
