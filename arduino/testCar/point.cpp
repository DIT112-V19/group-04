#include "point.h"

/*
 * Empty constructor for Point objects.
 * 
 * This constructor creates a new Point using the default coordinates. 
 */
Point::Point() {
  mx = DEFAULT_X;
  my = DEFAULT_Y;
}

/*
 * Standard constructor for Point objects.
 * 
 * Create a point at the coordinates (x,y)
 * @param x   x-coordinate of the point
 * @param y   y-coordinate of the point
 */
Point::Point(double x, double y) {
  mx = x;
  my = y;
}
