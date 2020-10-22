#from Motor2 import Motor
from vegaMotor import Motor
#from vegaServo import Servo
import busio, time
import signal
def main():
    motor=Motor()
    servo=Servo()
    try:
        print("try")
        motor.setup_PWM()
        motor.drive_forward()
        time.sleep(2)
        motor.drive_backward()
        time.sleep(2)
        motor.turn_right()
        time.sleep(2)
        motor.turn_left()
        time.sleep(2)
        motor.stop_motors() 
        time.sleep(1)
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
