#Author: K. van der Vliet
#Name: Mood Player - GUI
#Description: GUI for the Mood Player
#Last updated: 10 May 2020

#Import System module
import sys

#Import PyQt5 Application and Widget
from PyQt5.QtWidgets import QApplication, QWidget
#Import PyQt Image and Pixmap
from PyQt5.QtGui import QImage, QPixmap
#Import PyQt Timer
from PyQt5.QtCore import QTimer

#Import OpenCV
import cv2

#Custom
#Import the variables used by the GUI
import MoodPlayer_GUI_variables as GUI_var
#Import the functions used by the GUI
from MoodPlayer_GUI_functions import *

class MoodPlayer_GUI(QWidget):
	def __init__(self, title, fav_loc):
		super().__init__()
		#Run the Setup GUI function
		setup_GUI(self, title, fav_loc)

		#Create a timer
		self.timer = QTimer()
		#Connect timer to viewCam function
		self.timer.timeout.connect(self.viewCam)
		#Set contrBtn click function
		self.contrBtn.clicked.connect(self.startStopTimer)

	#View camera
	def viewCam(self):
		#Read image in BGR format
		ret, image = self.cap.read()
		#Convert image to RGB format
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		#Get image infos
		height, width, channel = image.shape
		step = channel * width
		#Create QImage from image
		qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
		#Show image in img_label
		self.image_label.setPixmap(QPixmap.fromImage(qImg))

	#Start/stop timer
	def startStopTimer(self):
		#If timer is stopped
		if not self.timer.isActive():
		#Create video capture
			self.cap = cv2.VideoCapture(0)
			#Start timer
			self.timer.start(20)
			#Set contrBtn text
			self.contrBtn.setText("Stop")
		#If timer is started
		else:
			#Stop timer
			self.timer.stop()
			#Release video capture
			self.cap.release()
			#Set contrBtn text
			self.contrBtn.setText("Start")


#Create application
app = QApplication(sys.argv)
#Fill in the parameters
mp = MoodPlayer_GUI(GUI_var.textTitle, GUI_var.src_fav)
#Show Mood Player GUI
mp.show()
sys.exit(app.exec_())