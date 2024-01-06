import RPi.GPIO as GPIO

GPIO.setmode(GPIO.Board)
GPIO.setup(15,GPIO.IN,GPIO.PUD_DOWN)
motion = GPIO.input(15)
print(motion)