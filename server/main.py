from flask import Flask, request, jsonify
from utils.nodefinder import node_finder
from utils.simulator import car_mover, simulator
from entities.carpool import Carpool
from entities.user import User
from entities.car import Car
from threading import Thread
import pickle


app = Flask(__name__)
carpool = Carpool()


@app.route('/api')
def get_all_data():
    # This endpoints will be used to retrieve all information about all cars and users
    return carpool.json(), 200


@app.route('/api/pickup', methods=['POST'])
def pickup():

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

    # Updates the users location with the ones send in the JSON payload
    user.update_location(location)

    car = carpool.logic(location, destination)
    if car:
        car.add_passenger(user)
        return jsonify({"carLocation": car.location.json()}), 200
    return "no car"


@app.route('/api/getlocation', methods=['GET'])
def get_location():

    user_id = request.headers['Cookie'][3:]

    # Finds or creates a user
    user = carpool.find_user(user_id)
    if user:
        for car in carpool.cars:
            for passenger in car.passengers:
                if passenger == user:
                    return jsonify({"carLocation": car.location.json()}), 200

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
    sim = simulator.Simulator(carpool)


carpool.graph = load_map()
a = Car("Car 1", node_finder(carpool.graph, 0, 0))
b = Car("Car 2", node_finder(carpool.graph, 1500, 200))
c = Car("Car 3", node_finder(carpool.graph, 2000, 1000))
carpool.cars.extend([a, b, c])
carpool.logic(node_finder(carpool.graph, 730, 1200), node_finder(carpool.graph, 2730, 100))

# Makes sure the following only gets executed once
if __name__ == '__main__':
    t1 = Thread(target=start_flask)
    t2 = Thread(target=run_car_mover)
    t3 = Thread(target=run_simulator)

    t1.start()
    t2.start()
    t3.start()

