
import cv2


cascade_src = 'haarcascades/haarcascade_frontalface_default.xml'
#video_src = 'videos/output.avi'
# video_src = 'dataset/video2.avi'

cap = cv2.VideoCapture(0)
car_cascade = cv2.CascadeClassifier(cascade_src)

while True:
    ret, img = cap.read(0)
    if (type(img) == type(None)):
        print("No Camera connected / Hardware issues")
        break

    #print(type(img),'12345')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    for (x, y, w, h) in cars:
        myrect = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)
        print(myrect)
        if myrect != []:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, 'Face', (x + w, y + h), font, 0.5, (11, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('video', img)

    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()