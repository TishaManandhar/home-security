import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(16,GPIO.OUT)
GPIO.output(16,GPIO.LOW)