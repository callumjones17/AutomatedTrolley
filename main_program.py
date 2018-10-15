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
        print("Going Left")
        #print(objSense.check(_LEFT))
        motCont.go_left(1)
    elif input == "1":
        print("Going Forward")
        #print(objSense.check(_FORWARD))
        motCont.go_forward(1)
    elif input == "3":
        print("Going Right")
        #print(objSense.check(_RIGHT))
        motCont.go_right(1)
    elif input == "4":
        print("Going Backward")
        #print(objSense.check(_BACKWARD))
        motCont.go_backward(2)
    else:
        print("Stopping")
        #print(objSense.check(_STOP))
        motCont.stop()