# Lab 11. Detect circle and lines
# Lim Gyu-yeon, 202334734, Dept. Computer science and engineering

import cv2
import numpy as np

src = cv2.imread("nevada.jpg")
dst = src.copy() # for Hough
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY) # for bi-finder
canny = cv2.Canny(gray, 5000, 1500, apertureSize = 5, L2gradient = True)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100, param1 = 250, param2 = 10, minRadius = 10, maxRadius = 50)

lines = cv2.HoughLinesP(canny, 0.8, np.pi / 180, 90, minLineLength = 10, maxLineGap = 80)

for i in circles[0]:
    cv2.circle(dst, (int(i[0]), int(i[1])), int(i[2]), (0, 0, 255), 5)
    
for i in lines:
    cv2.line(dst, (int(i[0][0]), int(i[0][1])), (int(i[0][2]), int(i[0][3])), (255, 0, 0), 2)

cv2.imshow("for lab11 - Lim Gyu-yeon", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()