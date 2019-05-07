from flask import Flask, request, jsonify
from utils.coordinate import Coordinate
from entities.carpool import Carpool
from entities.user import User

app = Flask(__name__)
carpool = Carpool()


@app.route('/api')
def get_all_data():
    # This endpoints will be used to retrieve all information about all cars and users
    return carpool.json(), 200


@app.route('/api/pickup', methods=['POST'])
def pickup():

    # Retrieves the cookie header and splits the string so only the value remains
    user_id = request.headers['Cookie'][3::]

    # Parses the JSON payload
    location = Coordinate(request.json["location"][0], request.json["location"][1])
    destination = Coordinate(request.json["destination"][0], request.json["destination"][1])

    # Finds or creates a user
    user = carpool.find_user(user_id)
    if user is None:
        user = User(user_id, location, destination)
        carpool.add_user(user)

    # Updates the users location with the ones send in the JSON payload
    user.update_location(location)

    return jsonify({"carLocation": carpool.find_car('real').location.json()}), 200


# Makes sure the following only gets executed once
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
