#include "bluetooth.h"

// constructor for Bluetooth module
Bluetooth::Bluetooth(HardwareSerial& connection) : 
  m_connection(connection),
  m_position(0) {}

void Bluetooth::init() {
  m_connection.begin(9600);
}


void Bluetooth::readSerial() {
  while (m_connection.available() > 0) {
    char data = m_connection.read();
    if (data == '\n' || m_position > 63) {
      parseCommand(m_buffer, m_position);
      memset(&m_buffer[0], 0, sizeof(m_buffer));    // erase the buffer's content
    } else {
      m_buffer[m_position] = data;
      m_position++;
    }
  }
}

/** 
 * 
 */
void Bluetooth::parseCommand(char *command, int length) {
  
}
