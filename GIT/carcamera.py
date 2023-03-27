import cv2
import sys
import math
import cv2 as cv
import numpy as np
import pafy
import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
LED1 = 11
GPIO.setup(LED1, GPIO.OUT, initial=GPIO.LOW)  
url = 'https://youtu.be/ipyzW38sHg0'
video = pafy.new(url)
best = video.getbest(preftype = 'mp4')

cap = cv2.VideoCapture(best.url)   

while (True):
    GPIO.output(LED1, GPIO.HIGH)

    ret, src = cap.read()

    src = cv2.resize(src, (640, 360))       
    src = cv2.flip(src,1)

    dst = cv.Canny(src, 50, 200, None, 3)

    cdst = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
    cdstP = np.copy(cdst)

    lines = cv.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)

    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
            pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
            cv.line(cdst, pt1, pt2, (0, 0, 255), 3, cv.LINE_AA)

    linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)
    
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0, 0, 255), 3, cv.LINE_AA)

    cv.imshow("Source", src)
    cv.imshow("Detected Lines (in red) - Standard Hough Line Transform", cdst)
    cv.imshow("Detected Lines (in red) - Probabilistic Line Transform", cdstP)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()