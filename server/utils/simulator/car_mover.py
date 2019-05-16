from math import sqrt, pow
import time

# velocity in m/s
CAR_VELOCITY = 13
# Whatever rate we choose
TICK_RATE = 0.2
CONVERSION_FACTOR = 1.542
DISTANCE_PER_TICK = CAR_VELOCITY*CONVERSION_FACTOR/TICK_RATE
RUNNING_STATE = False


def move_car(car):
    distance = 0
    while distance < DISTANCE_PER_TICK:
        if len(car.coordinates) < 2:
            break
        point = car.coordinates.pop(0)
        if point == car.destinations[0] or car.coordinates[0] == car.destinations[0]:
            car.destinations.pop(0)
        distance += sqrt(pow(car.coordinates[0].x - point.x, 2)+pow(car.coordinates[0].y - point.y, 2))
        car.location = car.coordinates[0]


def move_all_cars(carpool):
    lst = carpool.cars
    RUNNING_STATE = True

    for car in lst:
        if len(car.destinations) > 0:
            move_car(car)
            print(car)
    RUNNING_STATE = False


def run(carpool):
    while True:
        if not RUNNING_STATE:
            move_all_cars(carpool)
            time.sleep(1/TICK_RATE)
