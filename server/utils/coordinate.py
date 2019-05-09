class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __repr__(self):
        return str((self.x, self.y))

    def json(self):
        return [self.x, self.y]

    def to_string(self):
        return str(self.x) + ", " + str(self.y)
