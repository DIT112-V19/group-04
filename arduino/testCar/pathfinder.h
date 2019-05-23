#ifndef PATHCAR_H
#define PATHCAR_H

#include <Smartcar.h>
#include "bluetooth.h"
#include "constants.h"
#include <stdlib.h>

static const int DEG_IN_CIRCLE = 360;
static const int ANGLE_TOLERANCE = 5;

static const double DEFAULT_X = 0.0;
static const double DEFAULT_Y = 0.0;
static const double DEFAULT_THETA = 0.0;

class PathFinder {
private:
  HeadingCar m_car;
  Bluetooth m_connection;
  double m_x;
  double m_y;
  int m_heading;

  bool m_turn;
  int m_target_heading;
  
  bool m_drive;
  double m_target_distance; 


public:
  PathFinder(const HeadingCar& car, const Bluetooth& blue, double x, double y);
  PathFinder(HeadingCar car, Bluetooth blue) : PathFinder(car, blue, DEFAULT_X, DEFAULT_Y){};


  double getX() {return m_x;}
  double getY() {return m_y;}
  int getHeading() {return m_heading;};

  void init();
  void update();
  HardwareSerial getConnection() {return m_connection.getConnection();}
  
  void rotateOnSpot(int targetDegrees, int speed);
  void rotateToHeading(int targetHeading, int speed);
};

int trimHeading(int heading);

#endif
