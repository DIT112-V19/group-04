from flask import Flask, request, jsonify
from utils.coordinate import Coordinate
from entities import Carpool, User

app = Flask(__name__)
carpool = Carpool()


@app.route('/api/pickup', methods=['POST'])
def pickup():

    user_id = request.headers['Cookie'][3::]
    location = Coordinate(request.json["location"][0], request.json["location"][1])
    destination = Coordinate(request.json["destination"][0], request.json["destination"][1])

    user = carpool.find_user(user_id)
    if user is None:
        user = User(user_id, location, destination)
        carpool.add_user(user)

    user.update_location(location)

    carpool.print_all_users()
    carpool.print_all_cars()

    return jsonify({"carLocation": carpool.find_car('real').location.json()}), 200


# Makes sure the following only gets executed once
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
