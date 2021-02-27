import RPi.GPIO as GPIO
from time import sleep


Ena= 0 #Pin number
In1= 0 #Pin number
In2= 0 #Pin where PWM will be generated for varying the speed

#PIN SETUP

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#############################################################

GPIO.setup(Ena,GPIO.OUT) #sets the pin to output mode- motor 1
GPIO.setup(In1,GPIO.OUT) #motor 2
GPIO.setup(In2,GPIO.OUT) # pin for controlling the speed

pwmA=GPIO.PWM(pwmpin,100) #100 is frequency
pwmA.start(0) # basically setting speed as 0

#############################################################


pwmA.ChangeDutyCycle(60)  #accounts fro 60%
GPIO.output(In1,GPIO.LOW)
GPIO.output(In2,GPIO.HIGH)
sleep(2)
pwmA.ChangeDutyCycle(0);

