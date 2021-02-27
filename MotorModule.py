import Rpi.GPIO as GPIO
from time import sleep

class Motor():
    def __init__(self,EnaA,In1A,In2A,EnaB,In1B,In2B):
        self.EnaA=EnaA  #reference to the current instance of the calss and is used to access vairables that belongs to the class
        self.In1A=In1A
        self.In2A=In2A
        self.EnaB = EnaB  # reference to the current instance of the calss and is used to access vairables that belongs to the class
        self.In1B = In1B
        self.In2B = In2B
        GPIO.setup(self.EnaA, GPIO.OUT)
        GPIO.setup(self.In1A, GPIO.OUT)
        GPIO.setup(self.In2A, GPIO.OUT)
        GPIO.setup(self.EnaB, GPIO.OUT)
        GPIO.setup(self.In1B, GPIO.OUT)
        GPIO.setup(self.In2B, GPIO.OUT)
        self.pwmA=GPIO.PWM(self.EnaA,100);
        self.pwmA.start(0);
        self.pwmB = GPIO.PWM(self.EnaB, 100);
        self.pwmB.start(0);

    def moveF(self,speed=50,t=0):
        self.pwmA.ChangeDutyCycle(speed)  # accounts fro 60%
        GPIO.output(self.In1A, GPIO.LOW)
        GPIO.output(self.In2A, GPIO.HIGH)
        self.pwmB.ChangeDutyCycle(speed)  # accounts fro 60%
        GPIO.output(self.In1B, GPIO.LOW)
        GPIO.output(self.In2B, GPIO.HIGH)
        sleep(t)

    def stop(self,t=0):
        self.pwmA.ChangeDutyCycle(0);
        self.pwmB.ChangeDutyCycle(0);

        sleep(t)





def main():
    motor1.moveF(60, 2)
    motor1.stop(2)


if __name__=='__main__':
    motor1 = Motor(2, 3, 4,,, )  # FORMAT (pin for motor 1, pin numbers for motor 2)
    main()


