#This is then main Program, all smaller pieces contained in
#Other files.
import serial_module as serMod
import motor_pwm as motCont
from DEFs import _LEFT, _RIGHT, _BACKWARD, _FORWARD, _STOP
import checkSensors as objSense

GPIO.setwarnings(False)

#Main Loop
while 1:
    input = serMod.get_serial()
    if input == "2":
        min_distance = objSense.check(_LEFT)
		# Perhaps do a Serial println Here??
		#serMod.send_serial(min_distance)
		if min_distance == 0 or min_distance > 200:
			print("Going Left")
			motCont.go_left(1)
		else:
			print("Can't Move")
    elif input == "1":
        min_distance = objSense.check(_FORWARD)
		if min_distance == 0 or min_distance > 200:
			print("Going Forward")
			motCont.go_forward(1)
		else:
			print("Can't Move");
    elif input == "3":
        min_distance = objSense.check(_RIGHT)
		if min_distance == 0 or min_distance > 200:
			print("Going Right")
			motCont.go_right(1)
		else:
			print("Can't Move")
	# No Sensors on the Back, is this really a good idea??
    elif input == "4":
        min_distance = objSense.check(_BACKWARD))
		if min_distance == 0 or min_distance > 200:
			print("Going Backward")
			motCont.go_backward(2)
		else:
			print("Cant Move")
    else:
        print("Stopping")
        motCont.stop()