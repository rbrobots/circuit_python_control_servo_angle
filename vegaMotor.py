import RPi.GPIO as GPIO
import time

class Motor():

    def __init__(self):
        self.LWB=11
        self.LWF=13
        self.RWF=16
        self.RWB=18
        self.LWS=32
        self.RWS=33
        self.right_wheel_speed=0
        self.left_wheel_speed=0

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.LWB,GPIO.OUT)#LWB
        GPIO.setup(self.LWF,GPIO.OUT)#LWF
        GPIO.setup(self.RWF,GPIO.OUT)#RWF
        GPIO.setup(self.RWB,GPIO.OUT)#RWB
        GPIO.setup(self.LWS,GPIO.OUT)#EN1
        GPIO.setup(self.RWS,GPIO.OUT)#EN2
        print("Motor setup complete")

    def set_right_wheel_speed(self,speed):
        self.right_wheel_speed=speed

    def set_left_wheel_speed(self,speed):
        self.left_wheel_speed=speed

    def drive_forward(self):
        GPIO.output(self.LWB,GPIO.LOW)
        GPIO.output(self.RWB,GPIO.LOW)
        GPIO.output(self.LWF,GPIO.HIGH)
        GPIO.output(self.RWF,GPIO.HIGH)
        try:
            GPIO.PWM(self.LWS,self.left_wheel_speed)
            GPIO.PWM(self.RWS,self.right_wheel_speed)
        except:
            print("some errors were encountered")
        finally:
            print("clean up")

    def drive_backward(self):
        GPIO.output(self.LWF,GPIO.LOW)
        GPIO.output(self.RWF,GPIO.LOW)
        GPIO.output(self.LWB,GPIO.HIGH)
        GPIO.output(self.RWB,GPIO.HIGH)
        try:
            GPIO.output(self.LWS,self.left_wheel_speed)
            GPIO.output(self.RWS,self.right_wheel_speed)
        except:
            print("errors")
        finally:
            print("clean up")

    def turn_right(self):
        GPIO.output(self.LWF,GPIO.HIGH)
        GPIO.output(self.RWB,GPIO.HIGH)
        GPIO.output(self.LWB,GPIO.LOW)
        GPIO.output(self.RWF,GPIO.LOW)
        try:
            GPIO.output(self.LWS,self.left_wheel_speed)
            GPIO.output(self.RWS,self.right_wheel_speed)
        except:
            print("errors")
        finally:
            print("clean up")

    def turn_left(self):
        GPIO.output(self.RWF,GPIO.HIGH)
        GPIO.output(self.LWB,GPIO.HIGH)
        GPIO.output(self.RWB,GPIO.LOW)
        GPIO.output(self.LWF,GPIO.LOW)
        try:
            GPIO.output(self.LWS,self.left_wheel_speed)
            GPIO.output(self.RWS,self.right_wheel_speed)
        except:
            print("errors")
        finally:
            print("clean up")

    def stop_motors(self):
        GPIO.output(self.LWF,GPIO.LOW)
        GPIO.output(self.RWF,GPIO.LOW)
        GPIO.output(self.LWB,GPIO.LOW)
        GPIO.output(self.RWB,GPIO.LOW)
        set_left_wheel_speed(self,0)
        set_right_wheel_speed(self,0)
        GPIO.PWM(LWS,0)
        GPIO.PWM(RWS,0)
