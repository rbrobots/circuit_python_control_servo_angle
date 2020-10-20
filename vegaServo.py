from board import SCL, SDA
import busio, time
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo

class Servo():

    def __init__(self):
        self.i2c=busio.I2C(SCL,SDA)
        self.pca = PCA9685(self.i2c)
        self.pca.frequency = 50
        self.servo0 = servo.Servo(self.pca.channels[0], min_pulse=580, max_pulse=2480)
        self.servo1 = servo.Servo(self.pca.channels[1], min_pulse=580, max_pulse=2480)
        print("init complete")

    def testServo(self):
        for i in range(180):
            self.servo0.angle = i
        time.sleep(1)
        for i in range(180):
            self.servo0.angle = 180 - i
        time.sleep(1)
        for i in range(90):
            self.servo1.angle = i
        time.sleep(1)
        for i in range(90):
            self.servo1.angle = 90 -i
        time.sleep(1)
        self.pca.deinit()

    def servoToAngle(self,i,n):
        print("servoToAngle")

