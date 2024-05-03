import serial
port = serial.Serial("/dev/ttyUSB0", 115200)
port.write(b'5')
