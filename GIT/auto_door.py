import smbus
import RPi.GPIO as GPIO 
import time


PinTrig=29
PinEcho=31
duty_ratio= 0
MaxDuty= 12
PWMpin= 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PinTrig, GPIO.OUT) 
GPIO.setup(PinEcho, GPIO.IN)
GPIO.setwarnings(False)
GPIO.setup(PWMpin, GPIO.OUT) 
# Define some device parameters
I2C_ADDR = 0x27 # I2C device address
LCD_WIDTH = 16 # Maximum characters per line
# Define some device constants
LCD_CHR = 1 # Mode - Sending data
LCD_CMD = 0 # Mode - Sending command
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
LCD_BACKLIGHT = 0x08 # On
#LCD_BACKLIGHT = 0x00 # Off
ENABLE = 0b00000100 # Enable bit
# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005
#Open I2C interface
#bus = smbus.SMBus(0) # Rev 1 Pi uses 0
bus = smbus.SMBus(1) # Rev 2 Pi uses 1
def lcd_init():
# Initialise display
    lcd_byte(0x33,LCD_CMD) # 110011 Initialise
    lcd_byte(0x32,LCD_CMD) # 110010 Initialise
    lcd_byte(0x06,LCD_CMD) # 000110 Cursor move  direction
    lcd_byte(0x0C,LCD_CMD) # 001100 Display On,CursorOff, Blink Off 
    lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
    lcd_byte(0x01,LCD_CMD) # 000001 Clear display
time.sleep(E_DELAY)
def lcd_byte(bits, mode):
# Send byte to data pins
# bits = the data
# mode = 1 for data and 0 for command
    bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
    bits_low = mode | ((bits<<4) & 0xF0) | LCD_BACKLIGHT
# High bits
    bus.write_byte(I2C_ADDR, bits_high)
    lcd_toggle_enable(bits_high)
# Low bits
    bus.write_byte(I2C_ADDR, bits_low)
    lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
# Toggle enable
    time.sleep(E_DELAY)
    bus.write_byte(I2C_ADDR, (bits | ENABLE))
    time.sleep(E_PULSE)
    bus.write_byte(I2C_ADDR,(bits & ~ENABLE))
    time.sleep(E_DELAY)
def lcd_string(message,line):
    # Send string to display
    message = message.ljust(LCD_WIDTH," ")
    lcd_byte(line, LCD_CMD)
    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]),LCD_CHR)

def main():
    seg = [40,38,32,26,24,22,18,36] # GPIO pin
    GPIO.setup(seg, GPIO.OUT, initial=GPIO.LOW)

    fnd = [(1,1,1,1,1,0,1,0), #0
        (0,1,1,0,0,0,0,0), #1
        (1,1,0,1,1,1,0,0), #2
        (1,1,1,1,0,1,0,0), #3 
        (0,1,1,0,0,1,1,0), #4
        (1,0,1,1,0,1,1,0), #5
        (1,0,1,1,1,1,1,0), #6
        (1,1,1,0,0,0,1,0), #7
        (1,1,1,1,1,1,1,0), #8
        (1,1,1,0,0,1,1,0)] #9
    PinTrig=29
    PinEcho=31
    duty_ratio= 0
    MaxDuty= 12
    PWMpin= 12
    Servo=GPIO.PWM(PWMpin, 50) 
    Servo.start(0)

    startTime=0
    stopTime=0
# Main program block
# Initialise display
    lcd_init()
    while True:
        GPIO.output(PinTrig, False) 
        time.sleep(2)
        # Send some test
        lcd_string('Distance.',LCD_LINE_1)
        GPIO.output(PinTrig, True) 
        time.sleep(0.00001) 
        GPIO.output(PinTrig, False) 
        while GPIO.input(PinEcho) == 0: 
            startTime = time.time()
        while GPIO.input(PinEcho) == 1: 
            stopTime = time.time()
        Time_interval= stopTime - startTime
        Distance = Time_interval * 17000
        Distance = round(Distance, 1)
        len = str(Distance)
        cvtnum= 'distance:' + len +'cm'
        lcd_string(cvtnum,LCD_LINE_2)
        if Distance < 5 :
            lcd_string('Open door',LCD_LINE_1)
            Servo.ChangeDutyCycle(12)
            list_num= [3, 2, 1, 0]
            for i in list_num:
                GPIO.output(seg,fnd[i])
                time.sleep(1)
            #time.sleep(3)       
        if Distance >= 5 :
            lcd_string('Close door',LCD_LINE_1)
            Servo.ChangeDutyCycle(1)
            time.sleep(1)
            
    GPIO.cleanup()
        # Send some more text
       
      
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        lcd_byte(0x01, LCD_CMD)

