from flask import Flask
from server.bluetooth.serial_connection import SerialConnection

app = Flask(__name__)
connection = SerialConnection(conn_type='usb')

@app.route('/')
def index():
    return "Welcome to group-04 car sharing service"

@app.route('/move')
def move():
    cmd = "M"
    connection.write(cmd)
    return "We will make the car move"


app.run(host='0.0.0.0', port=5000, debug=True)
