#from Motor2 import Motor
from vegaMotor import Motor
#from vegaServo import Servo
import busio, time
import signal
def main():
    motor=Motor()
#    servo=Servo()
    try:
        print("try")
#        motor.setup_PWM()
#        motor.drive_forward()
#        time.sleep(2)
#        motor.drive_backward()
#        time.sleep(2)
#        motor.turn_right()
#        time.sleep(2)
#        motor.turn_left()
#        time.sleep(2)
#        motor.stop_motors() 
#        time.sleep(1)
#        motor.testServo()
        motor.servo_turn_to_angle(0,180)
        time.sleep(5)
        motor.servo_turn_to_angle(0,160)
        time.sleep(5)
        motor.servo_turn_to_angle(0,100)
        time.sleep(5)
        motor.servo_turn_to_angle(0,0)
        time.sleep(3)
        motor.servo_turn_to_angle(1,45)
        time.sleep(3)
        motor.servo_turn_to_angle(1,90)
        time.sleep(3)
        motor.servo_turn_to_angle(1,0)
#        motor.servo_turn_to_angle(1,90)

#        time.sleep(1)
#        motor.testServo()
#        servo.testServo()
    except ValueError:
        print("ValueError")
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except NameError:
        print("nameerror")
    except AttributeError:
        print("attributeerror")
    except:
        print("unknown exception occurred")
    finally:
        print("finally")

if __name__ == "__main__":
    main()
