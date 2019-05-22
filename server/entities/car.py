
class Car:

    def __init__(self, id, location):
        self.id = id
        self.location = location
        self.coordinates = [location]
        self.destinations = []
        self.passengers = []

    def __repr__(self):
        return "Id: " + self.id + ", Location: " + self.location.to_string()

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

