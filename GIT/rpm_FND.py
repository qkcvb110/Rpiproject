from gpiozero import Motor
import time

motor = Motor(forward=2, backward=3)

while True:
    print('모터 회전 방향 : Forward')
    motor.forward(speed=0.3)
    time.sleep(2)

    print('모터 회전 방향 : Backward')
    motor.backward(speed=1)
    time.sleep(5)

