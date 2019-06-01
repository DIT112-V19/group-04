from flask import Flask, request, jsonify
from utils.nodefinder import node_finder
from utils.simulator import car_mover, simulator
from entities.carpool import Carpool
from entities.user import User
from entities.car import Car
from threading import Thread
from utils.bluetooth.serial_connection import SerialConnection
import time as time
from utils import Coordinate
import pickle

app = Flask(__name__)
bluetooth = SerialConnection('bluetooth')
carpool = Carpool(bluetooth)



@app.route('/api')
def get_all_data():
    # This endpoint is intended for use with the remote visualisation.
    # This is used to retrieve all information about all cars and users waiting for pickup.
    return carpool.json(), 200


@app.route('/api/pickup', methods=['POST'])
def pickup():

    global smart_car
    # Retrieves the cookie header and splits the string so only the value remains
    user_id = request.headers['Cookie'][3:]

    # Parses the JSON payload
    location = node_finder(carpool.graph, request.json["location"][0], request.json["location"][1])
    destination = node_finder(carpool.graph, request.json["destination"][0], request.json["destination"][1])

    # Finds or creates a user
    user = carpool.find_user(user_id)
    if user is None:
        user = User(user_id, location, destination)
        carpool.add_user(user)

    # Updates the user's location with the ones send in the JSON payload
    user.update_location(location)

    car = carpool.logic(location, destination)
    if car:
        # If a car was found for the customer, then this customer is added as a passenger.
        car.add_passenger(user)

        # This returns the location of the car that was found.
        return jsonify({"carLocation": car.location.json()}), 200

    # This return message should be improved.
    # The intention is to return status that no car was found.
    return "no car"


@app.route('/api/getlocation', methods=['GET'])
def get_location():

    user_id = request.headers['Cookie'][3:]

    # Find if the user_id is valid.
    user = carpool.find_user(user_id)
    if user:
        # If the user exists then check if the user is a passenger.
        for car in carpool.cars:
            for passenger in car.passengers:
                if passenger == user:
                    # Only if the user is a passenger should the location of the car be provided.
                    # This is to prevent unauthorised tracking of vehicles.
                    return jsonify({"carLocation": car.location.json()}), 200
    # This return message should be improved.
    # The intention is to signal that the user isn't a valid passenger.
    return "Not a user"


def load_map():
    try:
        with open('utils/mapcreator/map.txt', 'rb') as infile:
            data = pickle.load(infile)
            infile.close()
            return data
    except EOFError:
        print("No map loaded")


def start_flask():
    app.run(host='127.0.0.1', port=5000)


def run_car_mover():
    car_mover.run(carpool)


def run_simulator():
    simulator.Simulator(carpool)


def update_coordinates():

    while True:
        pos = bluetooth.read()      # read all characters available via bluetooth
        if pos:
            for car in carpool.cars:
                if car.id == carpool.OUR_SMART_CAR:
                    car.location = node_finder(carpool.graph, pos.x, pos.y)   # set the ca
                    car.visited.append(car.location)
        time.sleep(0.005)




carpool.graph = load_map()
# Below is just placeholder content for testing purpose, this should be removed from final product.
smart_car = Car(carpool.OUR_SMART_CAR, node_finder(carpool.graph, 0, 0))
b = Car("Car 2", node_finder(carpool.graph, 1500, 200))
c = Car("Car 3", node_finder(carpool.graph, 2000, 1000))
carpool.cars.extend([smart_car, b, c])
carpool.logic(node_finder(carpool.graph, 730, 1200), node_finder(carpool.graph, 2730, 100))

# Makes sure the following only gets executed once
if __name__ == '__main__':
    t1 = Thread(target=start_flask)
    t2 = Thread(target=run_car_mover)
    t3 = Thread(target=run_simulator)
    t4 = Thread(target=update_coordinates)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
