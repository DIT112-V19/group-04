#include "bluetooth.h"

// constructor for Bluetooth module
Bluetooth::Bluetooth(const HardwareSerial *connection) : 
  mPosition(0) {
    mConnection = connection;
  }

void Bluetooth::init() {
  mConnection->begin(BAUD_RATE);
}


void Bluetooth::readSerial() {
  while (mConnection->available() > 0) {
    char data = mConnection->read();
    if (data == '\n' || mPosition > 63) {
      parseCommand(mBuffer, mPosition);
      memset(&mBuffer[0], 0, sizeof(mBuffer));    // erase the buffer's content
    } else {
      mBuffer[mPosition] = data;
      mPosition++;
    }
  }
}

void Bluetooth::println(String text) {
  mConnection->println(text);
}

/** 
 * 
 */
void Bluetooth::parseCommand(char *command, int length) {
  
}
