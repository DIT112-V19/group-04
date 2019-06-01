from math import sqrt, pow
from utils.nodefinder import node_finder
import time

# This is for simulating vehicle movement

# Velocity in m/s
CAR_VELOCITY = 13
# Whatever rate we choose
TICK_RATE = 1
CONVERSION_FACTOR = 1.542
DISTANCE_PER_TICK = CAR_VELOCITY*CONVERSION_FACTOR/TICK_RATE
RUNNING_STATE = False

OUR_SMART_CAR = "Car 1"


def move_car(car):
    if car.id == OUR_SMART_CAR:
        move_user_car(car)
    else:
        distance = 0
        while distance < DISTANCE_PER_TICK:
            if len(car.coordinates) < 2:
                if len(car.passengers) > 0:
                    car.passengers = []
                break
            point = car.coordinates.pop(0)
            if point == car.destinations[0] or car.coordinates[0] == car.destinations[0]:
                car.destinations.pop(0)
                for p in car.passengers:
                    if p.destination == point:
                        car.passengers.pop(car.passengers.index(p))
            distance += sqrt(pow(car.coordinates[0].x - point.x, 2)+pow(car.coordinates[0].y - point.y, 2))
            car.location = car.coordinates[0]


def move_all_cars(carpool):
    lst = carpool.cars
    global RUNNING_STATE
    RUNNING_STATE = True

    for car in lst:
        if len(car.destinations) > 0:
            if car.id == carpool.OUR_SMART_CAR:
                car = move_user_car(car)
            else:
                move_car(car)
    RUNNING_STATE = False


def move_user_car(car):
    """
    The user car is moved by the telemetry data sent by the smartcar.
    The only thing that needs to be done here is popping deprecated route points.
    :param car: the user car
    :return:
    """
    while len(car.visited) > 0:
        if len(car.coordinates) < 2:
            car.passengers = []
            return car
        else:
            point = car.coordinates[0]
            if car.visited[0] == point:
                car.visited.pop(0)
                car.coordinates.pop(0)

            if point == car.destinations[0]:
                car.destinations.pop()
                for p in car.passengers:
                    if p.destination == point:
                        car.passengers.pop(car.passengers.index(p))

    return car






def run(carpool):
    while True:
        if not RUNNING_STATE:
            move_all_cars(carpool)
            time.sleep(1/TICK_RATE)
