from serial import Serial
from server.bluetooth import module_config, host_pc

conn_types = ['bluetooth', 'usb']
default_type = conn_types[0]


class SerialConnection(Serial):
    """Class to establish a serial connection to the SmartCar.

    Serial connection to transmit and receive data
    """

    def __init__(self, conn_type=default_type):
        """Initialises a serial connection to the SmartCar using either bluetooth or usb.

        Parameters
        -----------
        conn_type : str
            the connection type of the serial connection
            default : bluetooth
        """

        # super().__init__(**kwargs)
        if conn_type not in conn_types:
            conn_type = default_type

        self.serial_settings = module_config['serial_port'][host_pc]
        self.Serial = Serial(self.serial_settings[conn_type])
        self.Serial.reset_input_buffer()    # disregard everything sent before the connection has benn established

        print("SerialConnection initialised using", conn_type)

    def read(self):
        return self.Serial.read()

    def write(self, msg):
        """Transmit messages using the serial connection. Encodes strings to byte-arrays"""
        self.Serial.write(msg.encode('ascii'))


# Test a connection
# TODO move this part to testing
"""
conn = SerialConnection(conn_types[1])
print(conn.read())
conn.write('move')
print(conn.read())"""