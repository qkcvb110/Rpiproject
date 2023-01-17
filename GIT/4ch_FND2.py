import RPi.GPIO as GPIO 
import time
import math 
# Trig=11 초음파 신호 전송핀 번호 지정 및 출력지정
# Echo=12 초음파 수신하는 수신 핀 번호 지정 및 입력지정
def main():
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
    PinTrig=11
    PinEcho=13
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(PinTrig, GPIO.OUT) 
    GPIO.setup(PinEcho, GPIO.IN)

    startTime=0
    stopTime=0

    while True:
        GPIO.output(PinTrig, False) 
        time.sleep(0.1)
        # trigger
        print ('Calculating Distance. 1 nanosec pulse')
        GPIO.output(PinTrig, True) 
        time.sleep(0.0000001) 
        GPIO.output(PinTrig, False) 
        # echo
        while GPIO.input(PinEcho) == 0: 
            startTime = time.time()
        while GPIO.input(PinEcho) == 1: 
            stopTime = time.time()
        Time_interval= stopTime - startTime
        Distance = Time_interval * 1700000
        Distance = round(Distance)
        print ('Distance => ', Distance, 'mm')
        print (int(math.floor(Distance%10)))
        D4=int(math.floor(Distance%10))
        print (int(math.floor((Distance/10)%10)))
        D3=int(math.floor((Distance/10)%10))
        print (int(math.floor((Distance/100)%10)))
        D2=int(math.floor((Distance/100)%10))
        print (int(math.floor((Distance/1000)%10)))
        D1=int(math.floor((Distance/1000)%10))
        # a = []
        # for i in str(Distance):
        #     a.append(i)
        #     #print(a)
        #     print(i)
        if(Distance):
            for i in range(1, 100000000000000000000000000000000000000000000): 
                GPIO.output(com1,GPIO.HIGH)
                GPIO.output(seg,fnd[D1])
                time.sleep(0.0000000001)
                GPIO.output(com1,GPIO.LOW)
                GPIO.output(com2,GPIO.HIGH)
                GPIO.output(seg,fnd[D2])
                time.sleep(0.0000000001)
                GPIO.output(com2,GPIO.LOW)
                GPIO.output(com3,GPIO.HIGH)
                GPIO.output(seg,fnd[D3])
                time.sleep(0.0000000001)
                GPIO.output(com3,GPIO.LOW)
                GPIO.output(com4,GPIO.HIGH)
                GPIO.output(seg,fnd[D4])
                time.sleep(0.0000000001)
                GPIO.output(com4,GPIO.LOW)
                break
            
    GPIO.cleanup()
if __name__ == '__main__':
    main()