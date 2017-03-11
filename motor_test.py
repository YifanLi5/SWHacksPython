from motor_control import Stepper

def main():
    with Stepper() as s:
        s.spin(5)

if __name__ == '__main__':
    main()