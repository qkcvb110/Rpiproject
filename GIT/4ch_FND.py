import RPi.GPIO as GPIO
import time
#bus = smbus.SMBus(1)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

com1 = 37
com2 = 35
com3 = 33
com4 = 31
com = [com1,com2,com3,com4]
seg = [40,38,36,32,26,24,22,18] # GPIO pin
GPIO.setup(seg, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(com, GPIO.OUT, initial=GPIO.LOW)


fnd = [(0,0,0,0,0,0,1,1), #0
    (1,0,0,1,1,1,1,1), #1
    (0,0,1,0,0,1,0,1), #2
    (0,0,0,0,1,1,0,1), #3 
    (1,0,0,1,1,0,0,1), #4
    (0,1,0,0,1,0,0,1), #5
    (0,1,0,0,0,0,0,1), #6
    (0,0,0,1,1,0,1,1), #7
    (0,0,0,0,0,0,0,1), #8
    (0,0,0,1,1,0,0,1)] #9
# while 1:
#     for i in range(0, 10):
#         GPIO.output(seg,fnd[i])
#         time.sleep(1)
 
# out_disp = 0

# while True:
#     j = 1
#     for i in range(0, 6, 1):
#         out_disp = data[j] << 8 | digit[i]
#         bus.write_word_data(addr, out_port, out_disp)
#         j += 1
#     time.sleep(0.00005)
while 1:
    GPIO.output(com1,GPIO.HIGH)
    GPIO.output(seg,fnd[1])
    time.sleep(0.00000001)
    GPIO.output(com1,GPIO.LOW)
    GPIO.output(com2,GPIO.HIGH)
    GPIO.output(seg,fnd[2])
    time.sleep(0.00000001)
    GPIO.output(com2,GPIO.LOW)
    GPIO.output(com3,GPIO.HIGH)
    GPIO.output(seg,fnd[3])
    time.sleep(0.00000001)
    GPIO.output(com3,GPIO.LOW)
    GPIO.output(com4,GPIO.HIGH)
    GPIO.output(seg,fnd[4])
    time.sleep(0.00000001)
    GPIO.output(com4,GPIO.LOW)

        

