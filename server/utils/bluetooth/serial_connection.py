from serial import Serial
from utils.bluetooth import module_config, host_pc

CLEAR = "F**K"
APPENDER = "<"
SEPARATOR = ","
CLOSER = ">"
END_COMMAND = "\n"

class SerialConnection(Serial):
    """Class to establish a serial connection to the SmartCar and transmit & receive data.

    The class is ideally using the configuration to adapt to the used device.
    """

    def __init__(self, connection_type='bluetooth'):
        """Construct a SerialConnection using either bluetooth or usb.

        :param connection_type: parameter specifying whether to connect via 'bluetooth' or 'usb'
        """

        if connection_type not in ['bluetooth', 'usb']:
            raise Exception('Connection type \'' + connection_type + '\' is not supported')

        self.serial_settings = module_config['computers'][host_pc]
        self.Serial = Serial(self.serial_settings[connection_type])
        self.Serial.reset_input_buffer()    # disregard everything sent before the connection has benn established
        print("SerialConnection initialised using", connection_type)

    def read(self):
        """

        :return:
        """
        return self.Serial.read()

    def write(self, msg):
        """Write a message to the specified serial_port.

        :param msg: the message to be written (encoded into 'ascii' bytes before)
        """
        # Transmit messages using the serial connection. Encodes strings to byte-arrays
        self.Serial.write(msg.encode('ascii'))

    def send_coordinate(self, coordinate):
        """Send a coordinate to the SmartCar to append it to the current path.

        :param coordinate: coordinate to be appended to the SmartCar path.
        """
        x = coordinate[0]
        y = coordinate[1]
        msg = APPENDER + str(x) + SEPARATOR + str(y) + CLOSER + END_COMMAND      # format the coordinate
        self.write(msg)

    def clear_path(self):
        """Calling this function signals the pathfinder to delete its current path.

        This could be done by sending any arbitrary character.
        A 4 character trigger ("F**K") has been chosen to prevent accidental deletion.
        """
        self.write(CLEAR + END_COMMAND)

    def send_path(self, path):
        """This function is used to forward paths of arbitrary length to the PathFinder.

        The function first clears the existing path. The passed path is not appended!
        :param path: list of coordinates to be handed to the SmartCar"""
        self.clear_path()
        for coordinate in path:
            self.send_coordinate(coordinate)

