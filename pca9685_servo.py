# This example moves a servo its full range (180 degrees by default) and then back.
from board import SCL, SDA
import busio, time
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo

i2c = busio.I2C(SCL, SDA)

# Create a simple PCA9685 class instance.
pca = PCA9685(i2c)
pca.frequency = 50

servo0 = servo.Servo(pca.channels[0], min_pulse=580, max_pulse=2480)
servo1 = servo.Servo(pca.channels[1], min_pulse=580, max_pulse=2480)
# This is an example for the Micro Servo - High Powered, High Torque Metal Gear:
#   https://www.adafruit.com/product/2307
# servo7 = servo.Servo(pca.channels[0], min_pulse=600, max_pulse=2400)
# This is an example for the Standard servo - TowerPro SG-5010 - 5010:
#   https://www.adafruit.com/product/155
# servo7 = servo.Servo(pca.channels[0], min_pulse=600, max_pulse=2500) # GOOD
# This is an example for the Analog Feedback Servo: https://www.adafruit.com/product/1404
# servo7 = servo.Servo(pca.channels[0], min_pulse=600, max_pulse=2600)

# The pulse range is 1000 - 2000 by default.
# servo7 = servo.Servo(pca.channels[0])

for i in range(180):
    servo0.angle = i
time.sleep(1)
for i in range(180):
    servo0.angle = 180 - i
time.sleep(1)
for i in range(160):
    servo1.angle = i
time.sleep(1)
for i in range(160):
    servo1.angle = 160 - i
pca.deinit()
