#ifndef PATHCAR_H
#define PATHCAR_H

#include <Smartcar.h>
#include <HardwareSerial.h>
#include "constants.h"
#include "usedpins.h"
#include "point.h"
#include <stdlib.h>
#include <math.h>

static const int ANGLE_TOLERANCE = 5;
static const double DEFAULT_THETA = 0.0;

static const int MAX_PATH_LENGTH = 100;
static const int BUFFER_SIZE = 64;

static const int SCALE = 4;

class PathFinder {
private:
  HeadingCar mCar;
  const HardwareSerial *mConnection;
  char mBuffer[BUFFER_SIZE];
  int mPosition;
  bool mPublishPos = true;
  
  const DirectionlessOdometer *mLeftOdo;
  const DirectionlessOdometer *mRightOdo;

  const SR04 *mFrontDist;

  Point mPos = Point(0, 0);
  Point mPrev = Point(0, 0);
  int mSpeed;
  int mHeading = 0;
  int mDistance = 0;

  bool mProximityAlert = false;

  bool mTurn = false;
  int mTargetHeading = 45;
  
  bool mDrive = false;
  int mTargetDistance = 0; 

  Point mPath[MAX_PATH_LENGTH];
  Point mDestination;
  bool mHasDestination = false;
  int mReadPosition = 0;
  int mWritePosition = 0;

public:
  PathFinder(const HeadingCar& car, const HardwareSerial *blue, const DirectionlessOdometer *leftOdo, const DirectionlessOdometer *rightOdo, const SR04 *ultrasound,  Point pos=Point(DEFAULT_X, DEFAULT_Y), int speed=SPEED);

  // getters and setters
  Point getPos() {return mPos;}
  void publishPos() {mPublishPos = true;};
  int getHeading() {return mHeading;};
  int getDistance() {return mDistance;};
  int getTargetDistance() {return mTargetDistance;};
  void setTargetDistance(int dist) {mTargetDistance = dist;};
  int getSpeed() {return mSpeed;};
  void setSpeed(int speed) {mSpeed = speed;};
  HardwareSerial getConnection() {return *mConnection;}
  
  void init();
  void update();
  void updatePosition();
  bool checkDist();

  // connectivity
  void publishPosition();
  void readSerial();
  void parseCommand(char *command, int length);

  // path manipulation
  void clearPath();  
  void addPoint(const Point point);
  void setNextGoal();

  // functions to move the car
  void rotateOnSpot(int targetDegrees);
  void rotateToHeading(int targetHeading);
  void moveForward(int distance);
  void goToPoint(Point destination);
  void stopCar();
};

int trimHeading(int heading);

#endif
