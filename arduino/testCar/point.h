#ifndef POINT_H
#define POINT_H

static const double DEFAULT_X = 0.0;
static const double DEFAULT_Y = 0.0;

class Point {
private:
  double mx;
  double my;

public:
  /**
   * Standard constructor for Point objects.
   * 
   * Create a point at the coordinates (x,y)
   * @param x   x-coordinate of the point
   * @param y   y-coordinate of the point
   */
  Point(double x=DEFAULT_X, double y=DEFAULT_Y);

  double getX() {return mx;};
  void setX(double x) {mx = x;};
  double getY() {return my;};
  void setY(double y) {my = y;};
  void set(double x, double y) {setX(x); setY(y);};
};

#endif
