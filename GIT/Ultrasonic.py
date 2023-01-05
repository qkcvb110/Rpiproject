import RPi.GPIO as GPIO 
import time 
# Trig=11 초음파 신호 전송핀 번호 지정 및 출력지정
# Echo=12 초음파 수신하는 수신 핀 번호 지정 및 입력지정
def main():
    PinTrig=29
    PinEcho=31
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(PinTrig, GPIO.OUT) 
    GPIO.setup(PinEcho, GPIO.IN)

    startTime=0
    stopTime=0

    while True:
        GPIO.output(PinTrig, False) 
        time.sleep(2)
        # trigger
        print ('Calculating Distance. 1 nanosec pulse')
        GPIO.output(PinTrig, True) 
        time.sleep(0.00001) 
        GPIO.output(PinTrig, False) 
        # echo
        while GPIO.input(PinEcho) == 0: 
            startTime = time.time()
        while GPIO.input(PinEcho) == 1: 
            stopTime = time.time()
        Time_interval= stopTime - startTime
        Distance = Time_interval * 17000
        Distance = round(Distance, 2)
        print ('Distance => ', Distance, 'cm')
    GPIO.cleanup()
if __name__ == '__main__':
    main()