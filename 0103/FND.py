import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

seg = [40,38,32,26,24,22,18,36] # GPIO pin
GPIO.setup(seg, GPIO.OUT, initial=GPIO.LOW)

fnd = [(1,1,1,1,1,0,1,0), #0
    (0,1,1,0,0,0,0,0), #1
    (1,1,0,1,1,0,1,0), #2
    (1,1,1,1,1,0,1,0), #3 
    (0,1,1,0,0,1,1,0), #4
    (1,0,1,1,0,1,1,0), #5
    (1,0,1,1,1,1,1,0), #6
    (1,1,1,0,0,1,0,0), #7
    (1,1,1,1,1,1,1,0), #8
    (1,1,1,0,0,1,1,0)] #9

GPIO.output(seg,fnd[1])


