from entities.car import Car
from entities.user import User
from flask import jsonify
from utils.pathfinding import astar
import itertools
import math


ARBITRARY_ANGLE = 45
ARBITRARY_STATIONARY_VEHICLE_CONSTRAINT = 1.2
MAXIMUM_ALLOWED_PASSENGERS = 4


class Carpool:

    def __init__(self, connection):
        self.users = []
        self.cars = []
        self.graph = {}
        self.connection = connection
        self.OUR_SMART_CAR = "Car 1"

    def find_car(self, id):
        for car in self.cars:
            if car.id == id:
                return car
        return None

    def add_car(self, car):
        if isinstance(car, Car):
            print("adding car")
            self.cars.append(car)
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
        potential_cars = []

        for car in self.cars:
            # Rough filter to reduce the number of cars that we check
            # Find cars that are standing still or moving in roughly the same direction as customer vector.
            # ARBITRARY_ANGLE can be tweaked for desired results.
            if len(car.destinations) == 0:
                # this means that the car is stationary
                # maybe we can add some sort of distance filter
                potential_cars.append(car)

            else:
                # this means that the car is moving
                car_final_destination = car.destinations[-1]
                car_direction = calc_direction(car.location, car_final_destination)
                customer_direction = calc_direction(start, destination)
                angle_difference = math.fabs(car_direction - customer_direction)

                if angle_difference < ARBITRARY_ANGLE:
                    if len(car.passengers) < MAXIMUM_ALLOWED_PASSENGERS:
                        potential_cars.append(car)

        if len(potential_cars) > 0:
            # All cars travelling in the wrong direction have been filtered.
            # Now we look for the vehicle that will have the shortest path.
            # Currently no distance restrictions are implemented.
            # Just an arbitrary weight to reduce likelihood of picking a stationary vehicle over a moving one.
            # This means that no matter how much distance it adds it's still acceptable.

            distance_added = math.inf
            selected_array = None
            selected_car = None
            selected_destinations = None

            for car in potential_cars:

                paths, distance, destinations = self.generate_customer_path(car.location, car.destinations, start, destination)

                if distance < distance_added:
                    selected_car = car
                    selected_array = paths
                    selected_destinations = destinations
                    distance_added = distance

            selected_car.destinations = selected_destinations
            selected_car.coordinates = selected_array

            # If the car is the one represented by our SmartCar, we forward the new path
            print(selected_car.id)

            if selected_car.id == self.OUR_SMART_CAR:
                print(selected_car.coordinates)
                selected_car.coordinates.pop(0)
                self.connection.send_path(selected_car.coordinates)

            return selected_car

        else:
            return None

    def generate_customer_path(self, car_position, car_destinations, customer_start, customer_goal):
        points = [car_position, customer_start, customer_goal]+car_destinations
        permutations = itertools.permutations(points)
        valid_permutations = []

        # This generates all valid permutations of points to reach as not all permutations are valid

        for i in permutations:

            if i.index(customer_start) < i.index(customer_goal) and i.index(car_position) == 0:
                valid_permutations.append(i)

        path = []
        cost = math.inf
        destinations = []

        # This generates the paths for each of the permutations and picks the permutation with the least cost.

        for i in valid_permutations:
            new_path = []
            new_destinations = []
            new_cost = 0
            for j in i:
                # Generates the path and cost for every segment in the current permutation.
                # Then concatenates the segment to the total of the permutation for a complete path.
                if i.index(j) < len(i) - 1:
                    partial_path, partial_cost = astar.run(self.graph, i[i.index(j)], i[i.index(j) + 1])
                    new_path += partial_path
                    new_cost += partial_cost
                new_destinations.append(j)
            # If the new path is cheaper than the current cheapest path then this path replaces the old.
            if new_cost < cost:
                path = new_path
                cost = new_cost
                # As the first point of the new_destinations list is the current location, this should not be appended.
                destinations = new_destinations[1:]

        return path, cost, destinations


def calc_direction(coordinate1, coordinate2):
    # flipped x and y instead of subtracting pi/2
    direction = math.atan2(coordinate2.x-coordinate1.x, coordinate2.y-coordinate1.y)
    if direction < 0:
        direction += 2*math.pi

    return math.degrees(direction)
