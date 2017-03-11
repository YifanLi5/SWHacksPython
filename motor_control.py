from datetime import datetime
import time
import RPi.GPIO as GPIO
import sys

class Stepper():
    def __init__(self, mode = "Default", period = 3.0/2000.0):
        self.mode = mode
        self.initialized = False
        self.period = period
        self.step_pins = [37,35,33,31]

    def spin(self, duration = 5):
        """Duration is in seconds. Blocks until completion"""
        if self.initialized == False:
            print("[E] Stepper did not initialize correctly, not spinning",
                  file = sys.stderr)
            time.sleep(duration)
            return
        initial_time = datetime.utcnow()
        current_time = datetime.utcnow()
        step_counter = 0
        while (current_time - initial_time).seconds < duration:
            # TODO: get rid of step_counter (?)
            for pin in range(0, 4):
                xpin = self.step_pins[pin]
                if self.seq[step_counter][pin]!=0:
                    GPIO.output(xpin, True)
                else:
                    GPIO.output(xpin, False)
            step_counter += 1

            # restart sequence
            if (step_counter == self.step_count):
                step_counter = 0
            time.sleep(self.period)
            current_time = datetime.utcnow()

    def __enter__(self):
        GPIO.setmode(GPIO.BOARD)
        for pin in self.step_pins:
            GPIO.setup(pin,GPIO.OUT)
            GPIO.output(pin, False)
        time.sleep(0.1)

        if self.mode == "Basic":
            self.step_count = 4
            self.seq = [[1,0,0,0],
                        [0,1,0,0],
                        [0,0,1,0],
                        [0,0,0,1]]
        elif self.mode == "Default":
            self.step_count = 8
            self.seq = [[1,0,0,0],
                        [1,1,0,0],
                        [0,1,0,0],
                        [0,1,1,0],
                        [0,0,1,0],
                        [0,0,1,1],
                        [0,0,0,1],
                        [1,0,0,1]]

        elif self.mode == "Torque":
            self.step_count = 4
            self.seq = [[0,0,1,1],
                        [1,0,0,1],
                        [1,1,0,0],
                        [0,1,1,0]]
        else:
            # don't set initialized flag, we don't know
            # which mode to use the motor in
            self.step_count = 0
            self.seq = [[0, 0, 0, 0]]
            print("[E] Please set the mode correctly", file = sys.stderr)
            return

        self.initialized = True

    def __exit__(self, type, value, traceback):
        GPIO.cleanup()

