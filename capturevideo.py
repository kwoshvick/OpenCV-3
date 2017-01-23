import numpy as np
import cv2

video_src  = 'assets/videos/kafcup-2013-02-17-14-43-15.mp4'

cap = cv2.VideoCapture(video_src)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if type(frame) == type(None):
        #print("H/w issues")
        #print(Exception)q
        break

    # Our operations on the frame come heregg
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.waitKey(0)
        #break
    else:
        continue

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
