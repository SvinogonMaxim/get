import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

led=26
button=13
GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN)

state=0

GPIO.output(led, state)
try:
    while True:
        if GPIO.input(button): 
            state=1 - state   
            GPIO.output(led,state)
            time.sleep(0.2)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup() 