from vegaMotor import Motor


def main():
    motor = Motor()
    try:
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
