import math
from utils import vector
# START_HEADING is north

START_HEADING = 0.0
# TURN_RADIUS is an arbitrary number
TURN_RADIUS = 0.5


class Car:

    def __init__(self, id, location):
        self.id = id
        self.location = location
        self.heading = START_HEADING
        self.vectors = []
        self.inner_angle = 0
        self.coordinates = []
        self.coordinates.append(location)

    def __repr__(self):
        return "Id: " + self.id + ", Location: " + self.location.to_string()

    def determine_turn_direction(self, new_heading):
        # turn_direction value 1 equals left turn
        # turn_direction value 0 equals right turn

        # probably to be scrapped but keeping it for now

        angle_difference = new_heading - self.heading
        if angle_difference < 0:
            angle_difference += math.degrees(2*math.pi)
        if angle_difference >= math.degrees(math.pi):
            turn_direction = 1
        else:
            turn_direction = 0
        inner_angle = self.heading - new_heading
        if inner_angle < 0:
            inner_angle += 180
        else:
            inner_angle -= 180
        self.inner_angle = math.fabs(inner_angle)
        self.heading = new_heading

        return turn_direction

    def drive(self):
        # currently just printing information for testing purposes.

        self.calculate_vectors()
        for v in self.vectors:
            print("heading: ", self.heading)
            print("turn direction: ", self.determine_turn_direction(v.direction))
            print("distance: ", v.magnitude)
            print("distance to radius turn: ", v.magnitude - self.radius_turn(self.inner_angle))
        print("final heading:", self.heading)

    def calculate_vectors(self):
        i = 1
        while i < len(self.coordinates):
            c1 = self.coordinates[i-1]
            c2 = self.coordinates[i]
            v1 = vector.Vector(c1, c2)
            self.vectors.append(v1)
            i += 1

    def radius_turn(self, angle):
        # probably to be scrapped
        distance = TURN_RADIUS/math.tan(math.radians(angle/2))
        return distance
