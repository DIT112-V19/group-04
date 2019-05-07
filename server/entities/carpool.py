from entities.car import Car
from entities.user import User
from utils.coordinate import Coordinate
from flask import jsonify


class Carpool:
    users = []
    cars = []

    def __init__(self):
        # Creating 4 cars, one is real and that's the one that will represent the physical car

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
