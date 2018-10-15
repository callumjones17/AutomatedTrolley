import RPi.GPIO as IO
import time

mot_left_pwm = 18
mot_right_pwm = 13
mot_left_dir = 15
mot_right_dir = 14

IO.setwarnings(False)
IO.setmode(IO.BCM)

IO.setup(mot_left_pwm,OUT)
IO.setup(mot_right_pwm,OUT)
IO.setup(mot_left_dir,OUT)
IO.setup(mot_right_dir,OUT)

GPIO.output(mot_left_dir,LOW)
GPIO.output(mot_right_dir,LOW)

mot_left = IO.PWM(mot_left_pwm,500)
mot_right = IO.PWM(mot_right_pwm,500)

mot_left.start(0)
mot.right.start(0)

def go_forward():
    GPIO.output(mot_left_dir,HIGH)
    GPIO.output(mot_right_dir,LOW)
    mot_left.ChangeDutyCylce(40)
    mot_right.ChangeDutyCycle(40)
    time.sleep(3)
    mot_left.ChangeDutyCycle(0)
    mot_right.ChangeDutyCycle(0)
    return

def go_left():
    GPIO.output(mot_left_dir,LOW)
    GPIO.output(mot_right_dir,LOW)
    mot_left.ChangeDutyCylce(40)
    mot_right.ChangeDutyCycle(40)
    time.sleep(3)
    mot_left.ChangeDutyCycle(0)
    mot_right.ChangeDutyCycle(0)
    return

def go_right():
    GPIO.output(mot_left_dir,HIGH)
    GPIO.output(mot_right_dir,HIGH)
    mot_left.ChangeDutyCylce(40)
    mot_right.ChangeDutyCycle(40)
    time.sleep(3)
    mot_left.ChangeDutyCycle(0)
    mot_right.ChangeDutyCycle(0)
    return

def go_backward():
    GPIO.output(mot_left_dir,LOW)
    GPIO.output(mot_right_dir,HIGH)
    mot_left.ChangeDutyCylce(40)
    mot_right.ChangeDutyCycle(40)
    time.sleep(3)
    mot_left.ChangeDutyCycle(0)
    mot_right.ChangeDutyCycle(0)
    return
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         

def go_left(speed):
    
    return
def go_right(speed):
    return
def go_forward(speed):
    return
def go_backward(speed):
    return
def stop():
    return