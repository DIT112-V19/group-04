#ifndef BLUETOOTH_H
#define BLUETOOTH_H
#include <Smartcar.h>
#include <HardwareSerial.h>
#include "constants.h"

class Bluetooth 
{
public:
  // construction and initialization
  Bluetooth(const HardwareSerial *connection);
  void init();

  
  void readSerial();
  /**
   * Given a command in the format defined by our group 
   * for sending information from the server to the app,
   * find out what is expected to be done by the car.
   * @param command   pointer to the char array containing the command
   * @param length    length of the command contained in the char array
   */
  void parseCommand(char *command, int length);

  // getters and setters
  HardwareSerial getConnection() {return *mConnection;}
  void println(String text);


private:
  HardwareSerial *mConnection;
  char mBuffer[64];
  int mPosition;
};

#endif
