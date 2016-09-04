import RPi.GPIO as GPIO
import time
INT1=11
INT2=12
INT3=13
INT4=15
GPIO.setmode(GPIO.BOARD)
GPIO.setup(INT1,GPIO.OUT)
GPIO.setup(INT2,GPIO.OUT)
GPIO.setup(INT3,GPIO.OUT)
GPIO.setup(INT4,GPIO.OUT)
GPIO.output(INT1,GPIO.LOW)
GPIO.output(INT2,GPIO.HIGH)
GPIO.output(INT3,False)
GPIO.output(INT4,False)
time.sleep(0.5)
GPIO.cleanup()
