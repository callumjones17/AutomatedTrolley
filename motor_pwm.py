import RPi.GPIO as GPIO
import time

mot_left_pwm = 24
mot_right_pwm = 23
mot_left_dir = 15
mot_right_dir = 14

IO.setwarnings(False)
IO.setmode(GPIO.BCM)

IO.setup(mot_left_pwm,GPIO.OUT)
IO.setup(mot_right_pwm,GPIO.OUT)
IO.setup(mot_left_dir,GPIO.OUT)
IO.setup(mot_right_dir,GPIO.OUT)

GPIO.output(mot_left_dir,GPIO.LOW)
GPIO.output(mot_right_dir,GPIO.LOW)

mot_left = GPIO.PWM(mot_left_pwm,500)
mot_right = GPIO.PWM(mot_right_pwm,500)

mot_left.start(0)
mot.right.start(0)

mot_delay_time = 1.8

def go_forward():
    GPIO.output(mot_left_dir,GPIO.HIGH)
    GPIO.output(mot_right_dir,GPIO.LOW)
    mot_left.ChangeDutyCycle(40)
    mot_right.ChangeDutyCycle(40)
    time.sleep(mot_delay_time)
    mot_left.ChangeDutyCycle(0)
    mot_right.ChangeDutyCycle(0)
    return

def go_left():
    GPIO.output(mot_left_dir,GPIO.LOW)
    GPIO.output(mot_right_dir,GPIO.LOW)
    mot_left.ChangeDutyCylce(40)
    mot_right.ChangeDutyCycle(40)
    time.sleep(mot_delay_time)
    mot_left.ChangeDutyCycle(0)
    mot_right.ChangeDutyCycle(0)
    return

def go_right():
    GPIO.output(mot_left_dir,GPIO.HIGH)
    GPIO.output(mot_right_dir,GPIO.HIGH)
    mot_left.ChangeDutyCylce(40)
    mot_right.ChangeDutyCycle(40)
    time.sleep(mot_delay_time)
    mot_left.ChangeDutyCycle(0)
    mot_right.ChangeDutyCycle(0)
    return

def go_backward():
    GPIO.output(mot_left_dir,GPIO.LOW)
    GPIO.output(mot_right_dir,GPIO.HIGH)
    mot_left.ChangeDutyCylce(40)
    mot_right.ChangeDutyCycle(40)
    time.sleep(mot_delay_time)
    mot_left.ChangeDutyCycle(0)
    mot_right.ChangeDutyCycle(0)
    return
         