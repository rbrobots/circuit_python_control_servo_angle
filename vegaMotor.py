#import RPi.GPIO as GPIO
from board import *
import time, digitalio, pulseio, sys, busio
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo

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
#        self.pwm_lw.frequency = 0
        self.pwm_rw.duty_cycle = 0
#        self.pmw_rw.frequency = 0
        print("Wheel motor setup complete")
        self.i2c=busio.I2C(SCL,SDA)
        self.pca=PCA9685(self.i2c)
        self.pca.frequency=50
        self.servo0=servo.Servo(self.pca.channels[0], min_pulse=580, max_pulse=2480)
        self.servo1=servo.Servo(self.pca.channels[1], min_pulse=580, max_pulse=2480)
        self.servo0_pos = 0 #keep track of pos of servo
        self.servo1_pos = 0
        print("Servo motor setup complete")

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
#        self.pwm_lw.frequency = 0
        self.pwm_lw.duty_cycle = 0
#        self.pwm_rw.frequency = 0
        self.pwm_rw.duty_cycle = 0

    def update_duty_cycle(self,c):
        self.duty_cycle=c

    def servo_turn_to_angle(self,i,n):#i is channel and n is angle
        print("n:",n)
        print("s0 pos:",self.servo0_pos)
        print("s1 pos:",self.servo1_pos)
        if i==0 and n<=180 and n>=0:#restrict motion to 180 degrees
            if n<self.servo0_pos:#if servo needs to move clockwise
                print("in first loop")
                for j in range(self.servo0_pos,n,-1):
                    print(j)
                    self.servo0.angle = j
            else:#if servo moves anti-clockwise
                for j in range(self.servo0_pos,n):
                    self.servo0.angle=j
                    print(j)
                time.sleep(1)
                self.servo0_pos = n
        elif i==1 and n<=90 and n>=0:#restrict motion to 90 degrees
            if n < self.servo1_pos:#clockwise
                for j in range(self.servo1_pos,n,-1):
                    self.servo1.angle = j
            else:#anti-clockwise
                for j in range(self.servo1_pos,n):
                    self.servo1.angle = j
                time.sleep(1)
            self.servo1_pos = n#set servo pos to current pos in memory
        else:
            print("Unknown input")
        print("Servo motion complete")

    def testServo(self):
        for i in range(180):
            self.servo0.angle=i
        time.sleep(1)
        for i in range(180):
            self.servo0.angle=180-i
        time.sleep(1)
        for i in range(90):
            self.servo1.angle=i
        time.sleep(1)
        for i in range(90):
            self.servo1.angle=90-i
        time.sleep(1)
        self.pca.deinit()
    def terminate_process(self):
        print("termination complete")
        exit(0)

