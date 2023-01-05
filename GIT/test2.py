
import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

LED1 = 11
LED2 = 12
LED3 = 13
Led= [LED1,LED2,LED3]
# GPIO.setup(LED1, GPIO.OUT, initial=GPIO.LOW)
# GPIO.setup(LED2, GPIO.OUT, initial=GPIO.LOW)
# GPIO.setup(LED3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Led, GPIO.OUT, initial=GPIO.LOW)
while 1:
    GPIO.output(LED1, GPIO.HIGH)
    time.sleep(1)   
    GPIO.output(LED1, GPIO.LOW)
    time.sleep(1)  
    GPIO.output(LED2, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED2, GPIO.LOW)
    time.sleep(1)  
    GPIO.output(LED3, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED3, GPIO.LOW)
    time.sleep(1)
