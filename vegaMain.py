#from vegaMotor import Motor
from vegaServo import Servo
import busio, time
import signal
def main():
#    motor=Motor()
    servo=Servo()
#    signal.signal(signal.SIGTERM,motor.terminate_process)#if signals disconnect, safely terminate process
#    signal.signal(signal.SIGINT,motor.terminate_process)
#    signal.signal(signal.SIGHUP,motor.terminate_process)
#    signal.signal(signal.SIGQUIT,motor.terminate_process)
    try:
        print("try")
#        servo.test_servo(6)
    except:
        print("Errors occurred")
    finally:
#        motor.terminate_process()
        print("finally")

if __name__ == "__main__":
    main()
