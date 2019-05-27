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

  
  

  // getters and setters
  HardwareSerial getConnection() {return *mConnection;}
  void println(String text);


private:
  HardwareSerial *mConnection;
};

#endif
