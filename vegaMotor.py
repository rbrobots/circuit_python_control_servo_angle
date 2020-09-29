import RPi.GPIO as GPIO
import time

class Motor():

    def __init__(self,LWB,LWF,RWF,RWB,LWS,RWS):
        print("initialised")
        self.LWB=LWB
        self.LWF=LWF
        self.RWF=RWF
        self.RWB=RWB
        self.LWS=LWS
        self.RWS=RWS

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11,GPIO.OUT)#LWB
        GPIO.setup(13,GPIO.OUT)#LWF
        GPIO.setup(16,GPIO.OUT)#RWF
        GPIO.setup(18,GPIO.OUT)#RWB
        GPIO.setup(32,GPIO.OUT)#EN1
        GPIO.setup(33,GPIO.OUT)#EN2

        GPIO.output(13,GPIO.HIGH)
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(11,GPIO.LOW)
        GPIO.output(18,GPIO.LOW)

    def drive_forward(self,speed):
        GPIO.output(LWF,speed)
        GPIO.output(RWF,speed)
        try:
            pwm0 = GPIO.PWM(LWS,speed)
            pwm1 = GPIO.PWM(RWS,speed)
        except:
            print("some errors were encountered")
        finally:
            print("clean up")

    def drive_backward(self,speed):
        GPIO.output(LWB,speed)
        GPIO.output(RWB,speed)
        try:
            pwm0
