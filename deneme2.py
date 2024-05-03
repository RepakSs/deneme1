import time
import serial
port = serial.Serial("/dev/ttyUSB0", 115200)
time.sleep(1)
port.write(b'2')
