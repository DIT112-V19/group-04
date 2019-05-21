from flask import Flask, request, jsonify
from utils.nodefinder import node_finder
from entities.carpool import Carpool
from entities.user import User
from entities.car import Car
import json
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
    json_data = json.loads(request.data)
    location = node_finder(carpool.graph, json_data["location"][0], json_data["location"][1])
    destination = node_finder(carpool.graph, json_data["destination"][0], json_data["destination"][1])

    # Finds or creates a user
    user = carpool.find_user(user_id)
    if user is None:
        user = User(user_id, location, destination)
        carpool.add_user(user)
    # Updates the users location with the ones send in the JSON payload
    user.update_location(location)

    car = carpool.logic(location, destination)
    if car:
        return jsonify({"carLocation": car.location.json()}), 200
    return "no car"


def load_map():
    try:
        with open('utils/map-creator/map.txt', 'rb') as infile:
            data = pickle.load(infile)
            infile.close()
            return data
    except EOFError:
        print("No map loaded")


carpool.graph = load_map()
a = Car("Car 1", node_finder(carpool.graph, 0, 0))
b = Car("Car 2", node_finder(carpool.graph, 1500, 200))
c = Car("Car 3", node_finder(carpool.graph, 2000, 1000))
carpool.cars.extend([a, b, c])

# Makes sure the following only gets executed once
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
