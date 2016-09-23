import numpy as np
import cv2


car_cascade = cv2.CascadeClassifier('haarcascades/cars.xml')

img = cv2.imread('images/8.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = car_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()