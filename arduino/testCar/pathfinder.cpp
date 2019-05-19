#include "pathfinder.h"


/*PathFinder::PathFinder(HeadingCar car) {
  PathFinder(car, DEFAULT_X, DEFAULT_Y, DEFAULT_THETA);
}*/

PathFinder::PathFinder(const HeadingCar& car, const Bluetooth& blue, double x, double y) :
    m_car(car),
    m_connection(blue),
    m_x(x),
    m_y(y) {
      m_heading = 0;
      m_turn = false;
      m_target_heading = 0;
      m_drive = false;
      m_target_distance = 0.0;
    }


void PathFinder::init() {
  m_connection.getConnection().begin(9600);
  m_connection.getConnection().println(m_heading, DEC);
  rotateToHeading(176, 30);
}

void PathFinder::update() {
  m_car.update();     // update to integrate the latest heading sensor readings
  m_heading = m_car.getHeading();   // in the scale of 0 to 360
  
  // check whether the heading is in an acceptable range
  if (m_turn) {
    int diff =  abs(m_target_heading - m_heading);
    if (diff < ANGLE_TOLERANCE || diff > DEG_IN_CIRCLE - ANGLE_TOLERANCE) {
      m_car.setSpeed(0);
      m_turn = false;
    }
  }
}

/*
void PathFinder::println(String text) {
  m_connection.println(text);
}*/

/**
   Rotate the car on spot at the specified degrees with the certain speed
   @param degrees   The degrees to rotate on spot. Positive values for clockwise
                    negative for counter-clockwise.
   @param speed     The speed to rotate
*/
void PathFinder::rotateOnSpot(int targetDegrees, int speed) {
  speed = smartcarlib::utils::getAbsolute(speed);
  targetDegrees %= 360; //put it on a (-360,360) scale
  if (!targetDegrees) return; //if the target degrees is 0, don't bother doing anything
  /* Let's set opposite speed on each side of the car, so it rotates on spot */
  if (targetDegrees > 0) { //positive value means we should rotate clockwise
    m_car.overrideMotorSpeed(speed, -speed); // left motors spin forward, right motors spin backward
  } else { //rotate counter clockwise
    m_car.overrideMotorSpeed(-speed, speed); // left motors spin backward, right motors spin forward
  }
  unsigned int initialHeading = m_car.getHeading(); //the initial heading we'll use as offset to calculate the absolute displacement
  int degreesTurnedSoFar = 0; //this variable will hold the absolute displacement from the beginning of the rotation
  while (abs(degreesTurnedSoFar) < abs(targetDegrees)) { //while absolute displacement hasn't reached the (absolute) target, keep turning 
    int currentHeading = getHeading(); 
    if ((targetDegrees < 0) && (currentHeading > initialHeading)) { //if we are turning left and the current heading is larger than the
      //initial one (e.g. started at 10 degrees and now we are at 350), we need to substract 360, so to eventually get a signed
      currentHeading -= 360; //displacement from the initial heading (-20)
    } else if ((targetDegrees > 0) && (currentHeading < initialHeading)) { //if we are turning right and the heading is smaller than the
      //initial one (e.g. started at 350 degrees and now we are at 20), so to get a signed displacement (+30)
      currentHeading += 360;
    }
    degreesTurnedSoFar = initialHeading - currentHeading; //degrees turned so far is initial heading minus current (initial heading
    //is at least 0 and at most 360. To handle the "edge" cases we substracted or added 360 to currentHeading)
  }
  m_car.setSpeed(0); //we have reached the target, so stop the car
}


/**
   Rotate the car on spot to the specified heading using the given speed
   Do this without blocking the thread (no loop)
   @param targetHeading   The final heading to rotate to on spot. Calculate whether to rotate 
                          clockwise or counter-clockwise depending on the current heading.
   @param speed     The speed to rotate with
*/
void PathFinder::rotateToHeading(int target_heading, int speed) {
  m_car.setSpeed(0);    // make sure to stop the car initially
  target_heading = trimHeading(target_heading);   // trim the heading into the desired range
  int current_heading = getHeading();

  int diff = target_heading - current_heading;
  // always turn the shortest direction
  if (diff > 180) {   
    diff -= DEG_IN_CIRCLE;      
  } else if (diff < -180) {
    diff += DEG_IN_CIRCLE;
  }

  // set the car to turning mode
  m_turn = true;
  m_target_heading = target_heading;

  // set the motors 
  if (diff > 0) { //positive value means we should rotate clockwise
    m_car.overrideMotorSpeed(speed, -speed); // left motors spin forward, right motors spin backward
  } else { //rotate counter clockwise
    m_car.overrideMotorSpeed(-speed, speed); // left motors spin backward, right motors spin forward
  }
}


int trimHeading(int heading) {
  // move negative heading into the range 0 -- DEG_IN_CIRCLE
  // modulo does not do this as desired
  while (heading < 0) {
    heading = heading + DEG_IN_CIRCLE;
  }

  // if the heading is to big, bring it back into the desired range
  while (heading >= DEG_IN_CIRCLE) {
    heading = heading - DEG_IN_CIRCLE;
  }

  return heading;
}
