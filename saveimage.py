import numpy
import cv2
import os

directory ='./images'
#os.chdir(directory)
#print(os.getcwd())
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)
print("Files in '%s': %s" % (cwd, files))
print(os.path.cwd())


#image = cv2.imread('1.jpg'),0)


#cv2.imshow('myWindow',image)
#myinput = cv2.waitKey(0)
#if myinput == 27:
#    cv2.destroyAllWindows()
#elif myinput == ord('s'):
#    cv2.imwrite('1.png',image)
#    cv2.destroyAllWindows()