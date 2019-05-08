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
            # Find vehicles that are standing still or moving in roughly the same direction as customer vector.
            # ARBITRARY_ANGLE can be tweaked for desired results.
            if len(v.vectors) == 1:
                potential_vehicles.append(v)

            else:
                angle_difference = math.fabs(v.vectors[0].direction - customer_vector.direction)
                if angle_difference < ARBITRARY_ANGLE:
                    potential_vehicles.append(v)

        if len(potential_vehicles) > 0:
            # All vehicles travelling in the wrong direction have been filtered.
            # Now we look for the vehicle that will have the shortest path.
            # Currently no distance restrictions are implemented for moving vehicles, only stationary.
            # This means that no matter how much distance it adds it's still acceptable.
            # This part only uses vector magnitudes as path checking, in reality these distances could be longer.
            # Maybe we should use the a-star method instead at a higher cost.
            distance_added = math.inf
            selected_array = None
            selected_vehicle = None

            for v in potential_vehicles:
                new_distance = 0
                if len(v.vectors) > 0:

                    vector_array = self.path_picker(v.vectors[0], customer_vector)

                    for i in vector_array:
                        new_distance += i.magnitude

                    if new_distance < distance_added:
                        selected_vehicle = v
                        selected_array = vector_array
                        distance_added = new_distance

                else:
                    vector_array = [vector.Vector(v.position, start), customer_vector]
                    for i in vector_array:
                        new_distance += i.magnitude

                    if new_distance < distance_added/ARBITRARY_STATIONARY_VEHICLE_CONSTRAINT:
                        selected_vehicle = v
                        selected_array = vector_array
                        distance_added = new_distance

            if len(selected_vehicle.vectors) > 1:
                # this is if the vehicle has more than 1 customer
                connection_vector = vector.Vector(selected_array[2].end_coordinate,
                                                  selected_vehicle.vectors[1].endCoordinate)
                selected_vehicle.vectors.pop(1)
                selected_vehicle.vectors.pop(0)
                selected_vehicle.vectors.insert(0, connection_vector)
                selected_vehicle.vectors = selected_array + selected_vehicle.vectors
            else:
                selected_vehicle.vectors = selected_array

        else:
            # this should probably be sent to the app
            print("Sorry no vehicles found.")

    def path_picker(self, vehicle_vector, customer_vector):
        # This creates all possible paths and determines which of the 3 valid paths is the shortest
        ab = vehicle_vector
        cd = customer_vector
        ac = vector.Vector(ab.start_coordinate, cd.start_coordinate)
        bc = vector.Vector(cd.start_coordinate, ab.end_coordinate)
        bd = vector.Vector(ab.end_coordinate, cd.end_coordinate)
        cb = vector.Vector(cd.start_coordinate, ab.end_coordinate)
        db = vector.Vector(cd.end_coordinate, ab.end_coordinate)

        option1 = ab.magnitude + bc.magnitude + cd.magnitude
        option2 = ac.magnitude + cb.magnitude + bd.magnitude
        option3 = ac.magnitude + cd.magnitude + db.magnitude

        if option1 < option2 and option1 < option3:
            return [ab, bc, cd]
        elif option2 < option1 and option2 < option3:
            return [ac, cb, bd]
        else:
            return [ac, cd, db]

    def generate_path(self, start, destination):
        path, cost = astar.run(self.graph, start, destination)

