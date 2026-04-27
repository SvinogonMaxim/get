import RPi.GPIO as GPIO
import time

p = [26, 20, 19, 16, 13, 12, 25, 11]

GPIO.setmode(GPIO.BCM)
GPIO.setup(p, GPIO.OUT, initial=0)

try:
    GPIO.output(p, [1, 1, 1, 1, 1, 1, 1, 1])
    time.sleep(30)
finally:
    GPIO.output(p, 0)
    GPIO.cleanup()
