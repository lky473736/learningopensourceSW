# Lab 11. Detect circle and lines
# Lim Gyu-yeon, 202334734, Dept. Computer science and engineering

import cv2

cat_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')

img = cv2.imread('cat.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cats = cat_cascade.detectMultiScale(gray, scaleFactor=1.3,
	minNeighbors=2, minSize=(20, 20))

for (x, y, w, h) in cats :
    print (x, y, w, h)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
print ('number of cats in image = ', len(cats))
cv2.imshow('img', img)
cv2.waitKey()

# i am using mac, so i should write the code below.
cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)