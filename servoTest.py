from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
import time

def main():
    print("in main function")
    kit.servo[0].angle=180
    time.sleep(1)
    kit.servo[0].angle=0
    time.sleep(1)
    kit.servo[0].angle=180
    time.sleep(1)
    kit.servo[0].angle=0
    time.sleep(1)

    #kit.continuous_servo[1].throttle =0

if __name__ == "__main__":
    main()

