class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def json(self):
        return [self.x, self.y]

    def to_string(self):
        return str(self.x) + ", " + str(self.y)
