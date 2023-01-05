9
import RPi.GPIO as GPIO 
import time  
def main():
    duty_ratio= 0
    MaxDuty= 12
    PWMpin= 12
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(PWMpin, GPIO.OUT) 
    Servo=GPIO.PWM(PWMpin, 50) 
    Servo.start(0)
    print('Wating for 1 sec') 
    time.sleep(1) 
    #print('Rotating at interval of 0-12 degrees’)
    while duty_ratio <= MaxDuty:
        Servo.ChangeDutyCycle(duty_ratio)
        time.sleep(2)
        duty_ratio+= 1

    if duty_ratio > MaxDuty:
        duty_ratio= 0
        Servo.ChangeDutyCycle(duty_ratio)

    Servo.stop()
    GPIO.cleanup()
    print('Everythings cleanup')
if __name__ == '__main__':
    main()