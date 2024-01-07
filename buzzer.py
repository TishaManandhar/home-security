import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
def alert():
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(16, GPIO.HIGH)
    time.sleep(4)
    GPIO.output(16, GPIO.LOW)


