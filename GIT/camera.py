import cv2
import numpy as np
import sys


cap=cv2.VideoCapture(0,cv2.CAP_V4L) 
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
	
while True:				
	ret,image  = cap.read()
	image = cv2.flip(image, 1) 
	cv2.imshow('CAMERA',image)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		img_captured = cv2.imwrite('test09.png', image)
	if cv2.waitKey(1) & 0xFF == ord('g'):
			cv2.destroyAllwindows()
			cap.release()
			break