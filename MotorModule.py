import Rpi.GPIO as GPIO
from time import sleep


motor1= 0 #Pin number
motor2= 0 #Pin number
pwmpin= 0 #Pin where PWM will be generated

#PIN SETUP

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor1,GPIO.OUT) #sets the pin to output mode- motor 1
GPIO.setup(motor2,GPIO.OUT) #motor 2
GPIO.setup("",GPIO.OUT) # pin for controlling the speed

GPIO.output("motor1",GPIO.LOW)
GPIO.output("motor2",GPIO.LOW)

pwm=GPIO.PWM(pwmpin,)



