from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to group-04 car sharing service"

@app.route('/distance', methods=['POST'])
def go_distance():
    #Example request of when a user wants to go somewhere, parsing start and end position
    data = request.json

    try:
        start_cordinates = data["startPosition"]
        end_cordinates = data["endPosition"]
    except:
        return jsonify({"message": "Error parsing json"}), 400

    print("We received a start position from a user: " + str(start_cordinates))
    print("We received a end position from a user: " + str(end_cordinates))
    return jsonify({"startPosition": start_cordinates, "endPosition": end_cordinates}), 200




@app.route('/move')
def move():
    #TODO: Make our car move
    return "We will make the car move"


app.run(host='0.0.0.0', port=5000, debug=True)

