from PySide.QtCore import *
from PySide.QtGui import *
import cv2
import sys
import numpy
import time
import threading


#video = 'CheyenneVAhospital.mpeg4'
video = 'videos/road.mp4'
car_cascade = cv2.CascadeClassifier('cascades/cars.xml')


class MainApp(QWidget):
    def __init__(self,parent=None):
        #QWidget.__init__(self)
        super(MainApp, self).__init__(parent)
        #self.video_size = QSize(320, 240)

        self.setup_ui()
        self.setup_camera()


    def setup_ui(self):
        """Initialize widgets.
        """
        self.image_label = QLabel()
        #self.image_label.setFixedSize(self.video_size)
        self.quit_button = QPushButton("Quit")
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.image_label)
        self.main_layout.addWidget(self.quit_button)
        self.setLayout(self.main_layout)

    def keyPressEvent(self, QKeyEvent):
        super(MainApp, self).keyPressEvent(QKeyEvent)
        cv2.waitKey(1) & 0xFF == ord('q')
        if 's' == QKeyEvent.text():

            self.timer.stop()
            #cv2.imwrite("cat2.png", self.cvImage)
        else:
            self.timer.start(30)
            #exit()
            #cv2.waitKey(0)
            #app.exit(1)

    def pause(self):
        cv2.waitKey(1)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     cv2.waitKey(0)
        #     # break
        # else:
        #     self.close()
        #exit()


    def setup_camera(self):
        """
        Initialize camera.
        """
        self.capture = cv2.VideoCapture(video)
        self.quit_button.clicked.connect(self.pause)
        #self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.video_size.width())
        #self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.video_size.height())
        # cap = cv2.VideoCapture(0)
        #
        # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 160);
        # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 120);
        #self.capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 160)
        #cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
       # width =

        #img = cv2.imread('images/8.png')



        # self.timer = QTimer()
        # self.timer.timeout.connect(self.display_video_stream)
        # self.timer.start(30)


        self.timer = QTimer()
        self.timer.timeout.connect(self.display_video_stream)
        self.timer.start(30)




    def display_video_stream(self):
        """
        Read frame from camera and repaint QLabel widget.
        """
        #self.capture = cv2.VideoCapture(0)
        _, frame = self.capture.read()
        if (type(frame) == type(None)):
            print('error')
            exit()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)

        for (x, y, w, h) in cars:
            myrect = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 2)
            print(myrect)
            if myrect != []:
                font = cv2.FONT_HERSHEY_SIMPLEX



        frame = cv2.flip(frame, 1)
        image = QImage(frame, frame.shape[1], frame.shape[0],
                       frame.strides[0], QImage.Format_RGB888)
        self.image_label.setPixmap(QPixmap.fromImage(image))







        # threads.append(t)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainApp()
    win.show()
    sys.exit(app.exec_())



