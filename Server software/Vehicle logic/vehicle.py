import coordinate
import vector


class Vehicle:

    def __init__(self, name):
        self.name = name
        self.position = coordinate.Coordinate(0, 0)
        self.route = []
        self.heading = 0

    def updatePosition(self):
        self.position.updateValues()





d = Vehicle("Car 1")

print(d.name)

a = coordinate.Coordinate(0, 0)
b = coordinate.Coordinate(3, 4)
c = vector.Vector(a, b)
print(c.info())


