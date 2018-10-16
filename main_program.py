#This is then main Program, all smaller pieces contained in
#Other files.
import serial_module as serMod
from DEFs import _LEFT, _RIGHT, _BACKWARD, _FORWARD, _STOP
#import checkSensors as objSense
import RPi.GPIO as GPIO
import time

mot_left_pwm = 24
mot_right_pwm = 23
mot_left_dir = 15
mot_right_dir = 14

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(mot_left_pwm,GPIO.OUT)
GPIO.setup(mot_right_pwm,GPIO.OUT)
GPIO.setup(mot_left_dir,GPIO.OUT)
GPIO.setup(mot_right_dir,GPIO.OUT)

GPIO.output(mot_left_dir,GPIO.LOW)
GPIO.output(mot_right_dir,GPIO.LOW)

mot_left = GPIO.PWM(mot_left_pwm,500)
mot_right = GPIO.PWM(mot_right_pwm,500)

mot_left.start(0)
mot_right.start(0)

mot_delay_time = 1.8

max_us_distance = 45

def go_forward():
	#mot_left.start(0)
	#mot_right.start(0)
	GPIO.output(mot_left_dir,GPIO.LOW)
	GPIO.output(mot_right_dir,GPIO.HIGH)
	mot_left.ChangeDutyCycle(40)
	mot_right.ChangeDutyCycle(40)
	time.sleep(mot_delay_time)
	mot_left.ChangeDutyCycle(0)
	mot_right.ChangeDutyCycle(0)
	#mot_left.stop()
	#mot_right.stop()
	return

def go_left():
	#mot_left.start(0)
	#mot_right.start(0)
	GPIO.output(mot_left_dir,GPIO.LOW)
	GPIO.output(mot_right_dir,GPIO.LOW)
	mot_left.ChangeDutyCylce(40)
	mot_right.ChangeDutyCycle(40)
	time.sleep(mot_delay_time)
	mot_left.ChangeDutyCycle(0)
	mot_right.ChangeDutyCycle(0)
	#mot_left.stop()
	#mot_right.stop()
	return

def go_right():
	#mot_left.start(0)
	#mot_right.start(0)
	GPIO.output(mot_left_dir,GPIO.HIGH)
	GPIO.output(mot_right_dir,GPIO.HIGH)
	mot_left.ChangeDutyCylce(40)
	mot_right.ChangeDutyCycle(40)
	time.sleep(mot_delay_time)
	mot_left.ChangeDutyCycle(0)
	mot_right.ChangeDutyCycle(0)
	#mot_left.stop()
	#mot_right.stop()
	return

def go_backward():
	#mot_left.start(0)
	#mot_right.start(0)
	GPIO.output(mot_left_dir,GPIO.HIGH)
	GPIO.output(mot_right_dir,GPIO.LOW)
	mot_left.ChangeDutyCylce(40)
	mot_right.ChangeDutyCycle(40)
	time.sleep(mot_delay_time)
	mot_left.ChangeDutyCycle(0)
	mot_right.ChangeDutyCycle(0)
	#mot_left.stop()
	#mot_right.stop()
	return

#Main Loop
while 1:
	#input = serMod.get_serial()
	input_data = input("Direction: ")
	if input == "left":#"2":
		#min_distance = objSense.check(_LEFT)
		#if min_distance == 0 or min_distance > max_us_distance:
		print("Going Left")
		motCont.go_left(1)
		#else:
		print("Can't Move")
	elif input == "forward":#"1":
		#min_distance = objSense.check(_FORWARD)
		#if min_distance == 0 or min_distance > max_us_distance:
		print("Going Forward")
		motCont.go_forward(1)
		#else:
		print("Can't Move");
	elif input == "right":#3":
		#min_distance = objSense.check(_RIGHT)
		#if min_distance == 0 or min_distance > max_us_distance:
		print("Going Right")
		motCont.go_right(1)
		#else:
		print("Can't Move")
	elif input == "backward":#4":
		#min_distance = objSense.check(_BACKWARD)
		#if min_distance == 0 or min_distance > max_us_distance:
		print("Going Backward")
		motCont.go_backward(2)
		#else:
		print("Cant Move")
    else:
        print("Stopping")
        motCont.stop()