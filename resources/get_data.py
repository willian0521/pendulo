import cv2
import numpy as np

cap = cv2.VideoCapture("pendulo.mp4")

ret, frame = cap.read()
fame_numb = 0
punto_suspension = np.array([1, 1])
valores = []
fps = cap.get(cv2.CAP_PROP_FPS)

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

    if circles is not None:
        theta = np.atan2(circles[0][0][0] - punto_suspension[0], circles[0][0][1] - punto_suspension[1])
        valores.append(np.array([frame_num / fps, theta]))
    frame_num += 1
    ret, frame = cap.read()
cap.release()