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
        self.right_wheel_speed=50#default to 50
        self.left_wheel_speed=50#default to 50
        self.duty_cycle=50
        GPIO.getmode()
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.LWB,GPIO.OUT)#LWB
        GPIO.setup(self.LWF,GPIO.OUT)#LWF
        GPIO.setup(self.RWF,GPIO.OUT)#RWF
        GPIO.setup(self.RWB,GPIO.OUT)#RWB
        GPIO.setup(self.LWS,GPIO.OUT)#EN1
        GPIO.setup(self.RWS,GPIO.OUT)#EN2
        self.pwm0=GPIO.PWM(self.LWS,self.left_wheel_speed)
        self.pwm1=GPIO.PWM(self.RWS,self.right_wheel_speed)
        self.pwm0.start(self.duty_cycle)
        self.pwm1.start(self.duty_cycle)
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

    def drive_backward(self):
        GPIO.output(self.LWF,GPIO.LOW)
        GPIO.output(self.RWF,GPIO.LOW)
        GPIO.output(self.LWB,GPIO.HIGH)
        GPIO.output(self.RWB,GPIO.HIGH)

    def turn_right(self):
        GPIO.output(self.LWF,GPIO.HIGH)
        GPIO.output(self.RWB,GPIO.HIGH)
        GPIO.output(self.LWB,GPIO.LOW)
        GPIO.output(self.RWF,GPIO.LOW)

    def turn_left(self):
        GPIO.output(self.RWF,GPIO.HIGH)
        GPIO.output(self.LWB,GPIO.HIGH)
        GPIO.output(self.RWB,GPIO.LOW)
        GPIO.output(self.LWF,GPIO.LOW)

    def stop_motors(self):
        GPIO.output(self.LWF,GPIO.LOW)
        GPIO.output(self.RWF,GPIO.LOW)
        GPIO.output(self.LWB,GPIO.LOW)
        GPIO.output(self.RWB,GPIO.LOW)
        set_left_wheel_speed(self,0)
        set_right_wheel_speed(self,0)
        GPIO.PWM(LWS,0)
        GPIO.PWM(RWS,0)
    def update_duty_cycle(self,c):
        self.duty_cycle=c
    def terminate_process(self):
        self.pwm0.stop()
        self.pwm1.stop()
        GPIO.cleanup()
        print("termination complete")
        exit(0)

