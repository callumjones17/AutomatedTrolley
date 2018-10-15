import RPi.GPIO as GPIO
import time

def selectSensor(port, S0, S1, S2, S3, En):
    binary = port
    #binary=bin(port)
    #print(port)
    #print(binary)
    GPIO.output(En,True)
    if binary[0] == "1":
         GPIO.output(S3,True)
    else:
        GPIO.output(S3, False)
    if binary[1] == "1":
         GPIO.output(S2,True)
    else:
        GPIO.output(S2, False)
    if binary[2] == "1":
         GPIO.output(S1,True)
    else:
        GPIO.output(S1, False)
    if binary[3] == "1":
         GPIO.output(S0,True)
    else:
        GPIO.output(S0, False)
    time.sleep(0.01)
    GPIO.output(En,False)
    return 0


