#This is then main Program, all smaller pieces contained in
#Other files.
import serial_module as serMod
from DEFs import _LEFT, _RIGHT, _BACKWARD, _FORWARD, _STOP
#import checkSensors as objSense
import RPi.GPIO as GPIO
import time

mot_left_pwm = 13
mot_right_pwm = 18
mot_left_dir = 24
mot_right_dir = 23

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
	mot_left.ChangeDutyCycle(80)
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
	mot_left.ChangeDutyCycle(80)
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
	mot_left.ChangeDutyCycle(10)
	mot_right.ChangeDutyCycle(80)
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
	mot_left.ChangeDutyCycle(25)
	mot_right.ChangeDutyCycle(90)
	time.sleep(mot_delay_time)
	mot_left.ChangeDutyCycle(0)
	mot_right.ChangeDutyCycle(0)
	#mot_left.stop()
	#mot_right.stop()
	return

#Main Loop
while 1:
	#input = serMod.get_serial()
	input_data = raw_input("Direction: ")
	if input_data == "left":#"2":
		#min_distance = objSense.check(_LEFT)
		#if min_distance == 0 or min_distance > max_us_distance:
		print("Going Left")
		go_left()
		#else:
		print("Can't Move")
	elif input_data == "forward":#"1":
		#min_distance = objSense.check(_FORWARD)
		#if min_distance == 0 or min_distance > max_us_distance:
		print("Going Forward")
		go_forward()
		#else:
		print("Can't Move");
	elif input_data == "right":#3":
		#min_distance = objSense.check(_RIGHT)
		#if min_distance == 0 or min_distance > max_us_distance:
		print("Going Right")
		go_right()
		#else:
		print("Can't Move")
	elif input_data == "backward":#4":
		#min_distance = objSense.check(_BACKWARD)
		#if min_distance == 0 or min_distance > max_us_distance:
		print("Going Backward")
		go_backward()
		#else:
		print("Cant Move")
	else:
		print("Stopping")