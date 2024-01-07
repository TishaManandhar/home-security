import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(15,GPIO.IN,GPIO.PUD_DOWN)
GPIO.setwarnings(False)


def motion_detect():
    motion = GPIO.input(15)
    return motion == 1

