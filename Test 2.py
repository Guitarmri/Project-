import sys
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from PyQt5.QtWidgets import *
from PyQt5 import QtCore,QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QCoreApplication
class MyWindow(QMainWindow) :
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(800,450,310,80)
        self.setWindowTitle("Alzheime review")
        self.initUI()
    def initUI(self) :
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Select your file:")
        self.label.move(10,0)

        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Addfile")
        self.button.move(100,0)
        self.button.clicked.connect(self.clicked)
        
        button1 = QPushButton('Quit', self)
        button1.clicked.connect(QCoreApplication.instance().quit)
        button1.move(200, 0)       
        self.show()

    def clicked(self) :
        filename = askopenfilename()
        img=mpimg.imread(filename)
        imgplot = plt.imshow(img)
        im = cv2.imread(filename)
        bbox, label, conf = cv.detect_common_objects(im)
        output_image = draw_bbox(im, bbox, label, conf)
        plt.imshow(output_image)
        plt.show()
    
def window() :
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())

window()
