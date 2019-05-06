from serial import Serial
from bluetooth import module_config, host_pc


class SerialConnection(Serial):
    # Class to establish a serial connection to the SmartCar and transmit & receive data

    def __init__(self, connection_type='bluetooth'):

        if connection_type not in ['bluetooth', 'usb']:
            raise Exception('Connection type \'' + connection_type + '\' is not supported')

        self.serial_settings = module_config['serial_port'][host_pc]
        self.Serial = Serial(self.serial_settings[connection_type])
        self.Serial.reset_input_buffer()    # disregard everything sent before the connection has benn established
        print("SerialConnection initialised using", connection_type)

    def read(self):
        return self.Serial.read()

    def write(self, msg):
        # Transmit messages using the serial connection. Encodes strings to byte-arrays
        self.Serial.write(msg.encode('ascii'))
