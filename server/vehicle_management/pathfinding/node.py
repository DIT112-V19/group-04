import math
import vector


class Node:

    def __init__(self, position):
        self.position = position
        self.distance_to_goal = math.inf

    def calculate_distance_to_goal(self, goal):
        self.distance_to_goal = vector.Vector(self.position, goal).magnitude

    def __hash__(self):
        return hash(self.position)

    def __eq__(self, other):
        return self.position == other.position

    def __repr__(self):
        return str(self.position)
