import coordinate
import vector
import math


class Vehicle:

    def __init__(self, name, position, heading):
        self.name = name
        self.position = position
        self.route = []
        self.heading = heading


    def determineTurnDirection(self, newHeading):

        # turnDirection value 1 equals left turn
        # turnDirection value 0 equals right turn

        angleDifference = newHeading - self.heading

        if angleDifference < 0:
            angleDifference += math.degrees(math.pi * 2)
        if angleDifference >= math.degrees(math.pi):
            turnDirection = 1
        else:
            turnDirection = 0

        self.heading = newHeading

        return turnDirection

    def whereToDrive(self, destination):

        # self.position is assigned to destination for testing purposes.
        # this should be changed to update with information returned by the vehicle.
        # printing the updateHeading method to see turn direction for testing purposes.
        # printing path.magnitude to see the distance that should be driven, this should be transmitted to the vehicle.

        path = vector.Vector(self.position, destination)
        print(self.determineTurnDirection(path.direction))
        print(path.magnitude)
        self.position = destination


