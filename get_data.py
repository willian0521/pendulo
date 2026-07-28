import cv2
import numpy

cap = cv2.VideoCapture("pendulo.mp4")

ret, frame = cap.read()
fame_number = 0

while ret:

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (9, 9), 2)

    circles = cv2.HoughCircles(
        gray,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=50,
        param1=100,
        param2=30,
        minRadius=10,
        maxRadius=100
    )

    

    frame_num += 1