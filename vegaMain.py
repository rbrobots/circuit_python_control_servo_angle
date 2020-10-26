#from Motor2 import Motor
from vegaMotor import Motor
#from vegaServo import Servo
import busio, time
import signal
def main():
    motor=Motor()
#    servo=Servo()
    try:
#        motor.servo_turn(1,45)
#        motor.servo_turn(1,0)
#        motor.servo_terminate()
        print("try")
        motor.input_servo_value()
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
