import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT, initial=True)

GPIO.output(17, True)
time.sleep(5)
GPIO.output(17, False)
GPIO.cleanup()
print("test")




