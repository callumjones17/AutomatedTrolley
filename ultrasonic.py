#Common Pi Setup
import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)

def runSensor(TRIG, ECHO):
    
    pulse_end = 0
    pulse_start = 0
    
    #Get Inputs Ready
    #TRIG = 21
    #ECHO = 20
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG,False)
    time.sleep(0.1) #Give the input some time 

    #Send a 10uS pulse to the trigger pin
    GPIO.output(TRIG,True)
    time.sleep(0.0001)
    GPIO.output(TRIG,False)

    #Wait until the echo pin first goes high
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    #Wait until the echo pin finally goes low
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    #Calculate how long the pulse was in terms of time
    pulse_dur = pulse_end - pulse_start

    #Speed of sound is roughly 343m/s.
    #Time it takes for US is twice the distance to the object,
    #meaning that Speed = Distance/(Time*2)
    #17150 x time = Distance
    distance = pulse_dur * 17150
    distance = round(distance,2)

    #print"Distance",distance,"cm"
    
    #Common Pi Cleanup of pins
    return distance