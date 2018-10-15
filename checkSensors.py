from DEFs import _LEFT, _RIGHT, _BACKWARD, _FORWARD, _STOP
import RPi.GPIO as GPIO
import time
import multiplex as mx
import ultrasonic as us

GPIO.setmode(GPIO.BCM)

TRIG = 20
ECHO = 21

S0 = 6
S1 = 11
S2 = 19
S3 = 26
En = 5

NUM_US_SENSORS = 8

left_sensors = ["0000","0001","0010"]
front_sensors = ["0011","0101"]
right_sensors = ["0110","0111","1000"]


def check_right():
    min_distance = 0
        for sensor in right_sensors:
            mx.selectSensor(sensor, S0, S1, S2, S3, En)
            distance = (us.runSensor(TRIG,ECHO))
            if distance < min_distance:
                min_distance = distance
            time.sleep(0.01)
    return min_distance

def check_left():
    min_distance = 0
        for sensor in left_sensors:
            mx.selectSensor(sensor, S0, S1, S2, S3, En)
            distance = (us.runSensor(TRIG,ECHO))
            if distance < min_distance:
                min_distance = distance
            time.sleep(0.01)
    return min_distance

def check_front():
    min_distance = 0
        for sensor in front_sensors:
            mx.selectSensor(sensor, S0, S1, S2, S3, En)
            distance = (us.runSensor(TRIG,ECHO))
            if distance < min_distance:
                min_distance = distance
            time.sleep(0.01)
    return min_distance

def check_back():
    return 0

def check(direction):
    if (direction == _LEFT):
        return check_left()
    elif (direction == _RIGHT):
        return check_right()
    elif (direction == _FORWARD):
        return check_front()
    elif (direction == _BACKWARD):
        return check_back()
    else:
        return 0

