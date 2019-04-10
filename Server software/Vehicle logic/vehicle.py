import coordinate
import vector
import math


class Vehicle:

    def __init__(self, name):
        self.name = name
        self.position = coordinate.Coordinate(0, 0)
        self.route = []
        self.heading = 0.0

    def updatePosition(self):
        # Currently not in use
        self.position.updateValues()

    def determineTurnDirection(self, newHeading):

        # turnDirection value 0 equals left turn
        # turnDirection value 1 equals right turn

        angleDifference = newHeading - self.heading

        if angleDifference < 0:
            angleDifference += math.pi * 2
        if angleDifference >= math.pi:
            turnDirection = 1
        else:
            turnDirection = 0

        self.heading = newHeading

        return turnDirection

    def whereToDrive(self, destination):

        # self.position is assigned to destination for testing purposes.
        # this should be changed to update with information returned by the vehicle.
        # printing the updateHeading method to see turn direction for testing purposes.
        # printing path.magnitude to see the distance that should be driven.

        path = vector.Vector(self.position, destination)
        print(self.determineTurnDirection(path.direction))
        print(path.magnitude)
        self.position = destination



d = Vehicle("Car 1")



