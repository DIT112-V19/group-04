#ifndef PATHCAR_H
#define PATHCAR_H

#include <Smartcar.h>
#include <HardwareSerial.h>
#include "constants.h"
#include "usedpins.h"
#include "point.h"
#include <stdlib.h>
#include <math.h>

static const int DEG_IN_CIRCLE = 360;
static const int ANGLE_TOLERANCE = 5;

static const double DEFAULT_THETA = 0.0;

static const int MAX_PATH_LENGTH = 100;
static const int BUFFER_SIZE = 64;

static const int SCALE = 10;

static const char CLEAR_CMD[] = "F**K";
static const char APPENDER = '<';
static const char SEPARATOR = ',';
static const char CLOSER = '>';

class PathFinder {
private:
  HeadingCar mCar;
  const HardwareSerial *mConnection;
  char mBuffer[BUFFER_SIZE];
  int mPosition;
  bool mPublishPos = true;
  
  const DirectionlessOdometer *mLeftOdo;
  const DirectionlessOdometer *mRightOdo;

  const SR04 *frontDist;

  Point mPos = Point(0, 0);
  Point mPrev = Point(0, 0);
  int mSpeed;
  int mHeading = 0;
  int mDistance = 0;

  bool mTurn = false;
  int mTargetHeading = 45;
  
  bool mDrive = false;
  int mTargetDistance = 0; 

  Point mPath[MAX_PATH_LENGTH];
  int mReadPosition = 0;
  int mWritePosition = 0;

public:
  PathFinder(const HeadingCar& car, const HardwareSerial *blue, const DirectionlessOdometer *leftOdo, const DirectionlessOdometer *rightOdo, const SR04 *ultrasound,  Point pos, int speed=SPEED);
  PathFinder(const HeadingCar& car, const HardwareSerial *blue, const DirectionlessOdometer *leftOdo, const DirectionlessOdometer *rightOdo, const SR04 *ultrasound, int speed=SPEED) : 
                PathFinder(car, blue, leftOdo, rightOdo, ultrasound, Point(DEFAULT_X, DEFAULT_Y), speed){};


  Point getPos() {return mPos;}
  void publishPos() {mPublishPos = true;};
  int getHeading() {return mHeading;};
  int getDistance() {return mDistance;};
  int getTargetDistance() {return mTargetDistance;};
  void setTargetDistance(int dist) {mTargetDistance = dist;};
  int getSpeed() {return mSpeed;};
  void setSpeed(int speed) {mSpeed = speed;};
  

  void init();
  void update();
  void updatePosition();

  // connectivity
  HardwareSerial getConnection() {return *mConnection;}
  void publishPosition();
  void readSerial();
  /**
   * Given a command in the format defined by our group 
   * for sending information from the server to the app,
   * find out what is expected to be done by the car.
   * @param command   pointer to the char array containing the command
   * @param length    length of the command contained in the char array
   */
  void parseCommand(char *command, int length);

  void println(String text);
  
  void rotateOnSpot(int targetDegrees);
  void rotateToHeading(int targetHeading);

  void moveForward(int distance);
  void goToPoint(Point destination);
  void stopCar();

  void clearPath();  
  void addPoint(const Point point);
  void setNextGoal();
};

int trimHeading(int heading);

#endif
