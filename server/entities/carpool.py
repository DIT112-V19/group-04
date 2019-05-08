from entities.car import Car
from entities.user import User
from utils import Coordinate
from flask import jsonify
from utils import vector
from utils.pathfinding import astar
import math


ARBITRARY_ANGLE = 45
ARBITRARY_STATIONARY_VEHICLE_CONSTRAINT = 1.2


class Carpool:

    def __init__(self):
        # Creating 4 cars, one is real and that's the one that will represent the physical car
        self.users = []
        self.cars = []
        self.graph = {}

        car_loc = Coordinate(500, 500)
        car = Car('real', car_loc)
        self.cars.append(car)

        car_loc = Coordinate(1800, 1800)
        car = Car('fake', car_loc)
        self.cars.append(car)

        car_loc = Coordinate(300, 1500)
        car = Car('fake', car_loc)
        self.cars.append(car)

        car_loc = Coordinate(100, 800)
        car = Car('fake', car_loc)
        self.cars.append(car)

    def find_car(self, id):
        for car in self.cars:
            if car.id == id:
                return car
        return None

    def add_car(self, car):
        if isinstance(car, Car):
            print("adding car")
            self.users.append(car)
        else:
            print('not adding')

    def find_user(self, id):
        for user in self.users:
            if user.id == id:
                return user
        return None

    def add_user(self, user):
        if isinstance(user, User):
            print("adding user")
            self.users.append(user)
        else:
            print('not adding')

    def print_all_users(self):
        print("Current users")
        for user in self.users:
            print(user)

    def print_all_cars(self):
        print('Current cars')
        for car in self.cars:
            print(car)

    def json(self):
        cars = []
        users = []

        for car in self.cars:
            cars.append({
                "x": car.location.x,
                "y": car.location.y,
                "id": car.id
            })

        for user in self.users:
            users.append({
                "x": user.location.x,
                "y": user.location.y,
                "id": user.id
            })

        return jsonify({
            "cars": cars,
            "users": users
        })

    def logic(self, start, destination):
        potential_vehicles = []
        customer_vector = vector.Vector(start, destination)

        for v in self.cars:
            # Rough filter to reduce the number of cars that we check
            # Find cars that are standing still or moving in roughly the same direction as customer vector.
            # ARBITRARY_ANGLE can be tweaked for desired results.
            if len(v.destinations) == 0:
                # this means that the car is stationary
                # maybe we can add some sort of distance filter
                potential_vehicles.append(v)

            else:
                # this means that the car is moving

                angle_difference = math.fabs(vector.Vector(v.coordinates[0], v.destinations[0]).direction - customer_vector.direction)
                if angle_difference < ARBITRARY_ANGLE:
                    potential_vehicles.append(v)

        if len(potential_vehicles) > 0:
            # All cars travelling in the wrong direction have been filtered.
            # Now we look for the vehicle that will have the shortest path.
            # Currently no distance restrictions are implemented for moving cars, only stationary.
            # This means that no matter how much distance it adds it's still acceptable.

            distance_added = math.inf
            selected_array = None
            selected_vehicle = None
            selected_destinations = None

            for v in potential_vehicles:
                new_distance = 0
                if len(v.destinations) != 0:
                    # this means that the car has a customer
                    paths, distance, destinations = self.path_picker(v.coordinates[0], v.destinations[0],
                                                                     start, destination)
                    new_distance += distance

                    if new_distance < distance_added:
                        selected_vehicle = v
                        selected_array = paths
                        selected_destinations = destinations
                        distance_added = new_distance

                else:
                    # this is if the car has no customer
                    paths, distance, destinations = self.path_picker(v.coordinates[0], v.coordinates[0],
                                                                     start, destination)
                    new_distance = distance

                    if new_distance < distance_added/ARBITRARY_STATIONARY_VEHICLE_CONSTRAINT:
                        selected_vehicle = v
                        selected_array = paths
                        selected_destinations = destinations
                        distance_added = new_distance

            if len(selected_vehicle.destinations) > 1:
                # this is if the vehicle has more than 1 customer
                # then we generate a connection path between the new path and already existing path

                connection_path, cost = self.generate_path(selected_array[-1], selected_vehicle.destinations[1])
                d = selected_vehicle.destinations
                selected_vehicle.destinations = selected_destinations + d[d.index(connection_path[-1])+1:]
                c = selected_vehicle.coordinates
                selected_vehicle.coordinates = selected_array + connection_path + c[c.index()+1:]

            else:

                selected_vehicle.coordinates = selected_array
                selected_vehicle.destinations = selected_destinations

        else:
            # this should probably be sent to the app
            print("Sorry no vehicles found.")

    def generate_path(self, start, destination):
        path, cost = astar.run(self.graph, start, destination)
        return path, cost

    def path_picker(self, car_location, car_destination, customer_location, customer_destination):
        # This creates all possible paths and determines which of the 3 valid paths is the shortest
        ab = self.generate_path(car_location, car_destination)
        cd = self.generate_path(customer_location, customer_destination)
        ac = self.generate_path(car_location, customer_location)
        bc = self.generate_path(car_destination, customer_location)
        bd = self.generate_path(car_destination, customer_destination)
        cb = self.generate_path(customer_location, car_destination)
        db = self.generate_path(customer_destination, car_destination)

        option1 = ab[1] + bc[1] + cd[1]
        option2 = ac[1] + cb[1] + bd[1]
        option3 = ac[1] + cd[1] + db[1]
        destinations1 = ab[0][-1] + bc[0][-1] + cd[0][-1]
        destinations2 = ac[0][-1] + cb[0][-1] + bd[0][-1]
        destinations3 = ac[0][-1] + cd[0][-1] + db[0][-1]

        if option1 < option2 and option1 < option3:
            return ab[0] + bc[0] + cd[0], option1, destinations1
        elif option2 < option1 and option2 < option3:
            return ac[0] + cb[0] + bd[0], option2, destinations2
        else:
            return ac[0] + cd[0] + db[0], option3, destinations3



