import time
import serial

def get_serial():
    x=""
    while (x ==""):
        ser = serial.Serial(
        port='/dev/ttyS0',
        #port='/dev/rfcomm0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1)
	x=ser.readline()
	ser.close()
    return x
	
# def send_serial(data):
    # ser = serial.Serial(
    # port='/dev/ttyS0',
    # #port='/dev/rfcomm0',
    # baudrate = 9600,
    # parity=serial.PARITY_NONE,
    # stopbits=serial.STOPBITS_ONE,
    # bytesize=serial.EIGHTBITS,
    # timeout=1)
    # ser.write(data)
    # ser.close()
    # return