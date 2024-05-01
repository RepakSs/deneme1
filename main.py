import time

import serial

port = serial.Serial("/dev/ttyUSB0",115200)


print(port.name)

def test1():
    while True:
        veri = int(input("Değer Gir"))
        if veri == 1:
            port.write(b"a")
        if veri == 2:
            port.write(b"b")

def test2():
    while True:
        veri = port.readline()
        port.flushInput()
        print(veri)
        time.sleep(0.5)


test2()