import math


class Vector:

    def __init__(self, start_coordinate, end_coordinate):
        self.start_coordinate = start_coordinate
        self.end_coordinate = end_coordinate
        self.x = end_coordinate.x - start_coordinate.x
        self.y = end_coordinate.y - start_coordinate.y
        self.direction = self.calculate_direction()
        self.magnitude = self.calculate_magnitude()

    def calculate_magnitude(self):
        a = math.pow(self.x, 2)
        b = math.pow(self.y, 2)
        magnitude = math.sqrt(a+b)
        return magnitude

    def calculate_direction(self):
        # flipped x and y instead of subtracting pi/2
        direction = math.atan2(self.x, self.y)
        if direction < 0:
            direction += 2*math.pi

        return math.degrees(direction)
