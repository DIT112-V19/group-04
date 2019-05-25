#ifndef POINT_H
#define POINT_H

static const double DEFAULT_X = 0.0;
static const double DEFAULT_Y = 0.0;

class Point {
private:
  double mx;
  double my;

public:
  Point();
  Point(double x, double y);

  double getX() {return mx;};
  double getY() {return my;};
};


#endif
