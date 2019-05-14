class User():

    def __init__(self, id, location, destination):
        self.id = id
        self.location = location
        self.destination = destination

    def update_location(self, new_location):
        self.location = new_location

    def __repr__(self):
        return "Id: " + self.id + ", Location: " + self.location.to_string()