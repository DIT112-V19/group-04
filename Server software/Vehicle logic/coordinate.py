class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def updateValues(self):
        # this is to be used for data returned by the vehicle
        # currently not used
        self.x = int(input())
        self.y = int(input())

    def getX(self):
        return self.x

    def getY(self):
        return self.y
