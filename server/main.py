from flask import Flask, request, jsonify
from bluetooth.serial_connection import SerialConnection

app = Flask(__name__)
connection = SerialConnection(connection_type='usb')


@app.route('/')
def index():
    return "Welcome to group-04 car sharing service"


@app.route('/distance', methods=['POST'])
def go_distance():
    # Example request of when a user wants to gos somewhere, parsing start and end position
    data = request.json

    try:
        start_cordinates = data["startPosition"]
        end_cordinates = data["startPosition"]
    except:
        return jsonify({"message": "Error parsing json"}), 400

    print("We received a start position from a user: " + str(start_cordinates))
    print("We received an end position from a user: " + str(end_cordinates))
    return jsonify({"startPosition": start_cordinates, "endPosition": end_cordinates}), 200


@app.route('/move')
def move():
    cmd = "M"
    connection.write(cmd)
    return "We will make the car move"


# Makes sure the following only gets executed once
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
