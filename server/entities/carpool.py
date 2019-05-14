from entities.car import Car
from entities.user import User
from flask import jsonify
from utils import vector
from utils.pathfinding import astar
import itertools
import math


ARBITRARY_ANGLE = 45
ARBITRARY_STATIONARY_VEHICLE_CONSTRAINT = 1.2


class Carpool:

    def __init__(self):
        # Creating 4 cars, one is real and that's the one that will represent the physical car
        self.users = []
        self.cars = []
        self.graph = {}

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
                # perhaps add some maximum concurrent customer constraint
                angle_difference = math.fabs(vector.Vector(v.coordinates[0],
                                                           v.destinations[0]).direction - customer_vector.direction)
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
                if len(v.destinations) != 0:
                    # this means that the car has at least one customer
                    paths, distance, destinations = self.generate_customer_path(v.coordinates[0], v.destinations, start, destination)

                    if distance < distance_added:
                        selected_vehicle = v
                        selected_array = paths
                        selected_destinations = destinations
                        distance_added = distance

                else:
                    # this is if the car has no customer
                    paths, distance, destinations = self.generate_customer_path(v.coordinates[0], v.destinations, start, destination)

                    if distance < distance_added/ARBITRARY_STATIONARY_VEHICLE_CONSTRAINT:
                        selected_vehicle = v
                        selected_array = paths
                        selected_destinations = destinations
                        distance_added = distance

            selected_vehicle.destinations = selected_destinations
            selected_vehicle.coordinates = selected_array

        else:
            # this should probably be sent to the app
            print("Sorry no vehicles found.")

    def generate_customer_path(self, car_position, car_destinations, customer_start, customer_goal):
        points = [car_position, customer_start, customer_goal]+car_destinations
        permutations = itertools.permutations(points)
        valid_permutations = []

        for i in permutations:
            if i.index(customer_start) < i.index(customer_goal) and i.index(car_position) == 0:
                valid_permutations.append(i)

        path = []
        cost = math.inf
        destinations = []

        for i in valid_permutations:
            new_path = []
            new_destinations = []
            new_cost = 0
            for j in i:
                if i.index(j) < len(i) - 1:
                    partial_path, partial_cost = astar.run(self.graph, i[i.index(j)], i[i.index(j) + 1])
                    new_path += partial_path
                    new_cost += partial_cost
                new_destinations.append(j)
            if new_cost < cost:
                path = new_path
                cost = new_cost
                destinations = new_destinations

        return path, cost, destinations
