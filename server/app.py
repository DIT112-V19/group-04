from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to group-04 car sharing service"

@app.route('/move')
def move():
    #TODO: Make our car move
    return "We will make the car move"


app.run(host='0.0.0.0', port=5000, debug=True)
