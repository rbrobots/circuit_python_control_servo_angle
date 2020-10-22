#import RPi.GPIO as GPIO
from board import *
import time, digitalio, pulseio, sys, busio
#from adafruit_pca9685 import PCA9685
#from adafruit_motor import servo

class Motor():

    def __init__(self):
        self.LWB=digitalio.DigitalInOut(D17)
        self.LWF=digitalio.DigitalInOut(D27)
        self.RWF=digitalio.DigitalInOut(D23)
        self.RWB=digitalio.DigitalInOut(D24)
        self.right_wheel_speed=50#default to 50
        self.left_wheel_speed=50#default to 50
        self.duty_cycle=50
        self.LWB.direction = digitalio.Direction.OUTPUT
        self.LWF.direction = digitalio.Direction.OUTPUT
        self.RWF.direction = digitalio.Direction.OUTPUT
        self.RWB.direction = digitalio.Direction.OUTPUT
        self.pwm_lw = pulseio.PWMOut(D12)
        self.pwm_rw = pulseio.PWMOut(D13)
        self.pwm_lw.duty_cycle = 0
        self.pwm_rw.duty_cycle = 0
        print("Wheel motor setup complete")

    def drive_forward(self):
        print("in drive forward")
        self.LWB.value = False
        self.RWB.value = False
        self.RWF.value = True
        self.LWF.value = True
        print("drive forward complete")
    
    def setup_PWM(self):
        print("in test motors")
        self.pwm_lw.frequency = 100#defaults to 100 Hz
        self.pwm_rw.frequency = 100
        print("set frequency")
        self.pwm_lw.duty_cycle = 32767#defaults to 50% duty cycle
        self.pwm_rw.duty_cycle = 32767
        print("set duty")

    def set_right_wheel_speed(self,speed):
        self.right_wheel_speed=speed

    def set_left_wheel_speed(self,speed):
        self.left_wheel_speed=speed

    def drive_backward(self):
        print("drive")
        self.RWF.value = False
        self.LWF.value = False
        self.RWB.value = True
        self.LWB.value = True

    def turn_right(self):
        print("right")
        self.LWF.value = False
        self.RWB.value = False
        self.LWB.value = True
        self.RWF.value = True
        
    def turn_left(self):
        print("left")
        self.LWB.value = False
        self.RWF.value = False
        self.LWF.value = True
        self.RWB.value = True

    def stop_motors(self):
        print("stop")
        self.LWF.value = False
        self.LWB.value = False
        self.RWF.value = False
        self.RWB.value = False
        self.pwm_lw.frequency = 0
        self.pwm_lw.duty_cycle = 0
        self.pwm_rw.frequency = 0
        self.pwm_rw.duty_cycle = 0

    def update_duty_cycle(self,c):
        self.duty_cycle=c
    def terminate_process(self):
        print("termination complete")
        exit(0)

