#Author: K. van der Vliet
#Name: Mood Player - GUI Functions
#Description: GUI Functions for the Mood Player
#Last updated: 10 May 2020

#Import PyQt GUI
from PyQt5 import QtGui
#Import PyQt widgets
from PyQt5.QtWidgets import QGridLayout, QPushButton, QLabel
#Import PyQt Qt
from PyQt5.QtCore import Qt

#Define function for GUI setup
def setup_GUI(class_name, title, fav_loc):
	#Set window title
	class_name.setWindowTitle(title)
	#Set window icon
	class_name.setWindowIcon(QtGui.QIcon(fav_loc))

	#Create a grid layout
	layout = QGridLayout()

	#Set the layout to horizontal box
	class_name.setLayout(layout)
	#Create a button for start/stop
	class_name.contrBtn = QPushButton(class_name)
	#Set the text on the button to start
	class_name.contrBtn.setText("Start")
	#Create image label for the webcam view
	class_name.image_label = QLabel(class_name)

	#Create a text label for the explanation
	class_name.lblExpl = QLabel(class_name)
	#Set the text of the Explanation label
	class_name.lblExpl.setText("Short Explanation: This program plays music accordingly to the users mood. Press 'Start' to begin.")
	#Set the text alignment for the Explanation label
	class_name.lblExpl.setAlignment(Qt.AlignCenter)

	#Create a text label for the Spotify Playlist
	class_name.lblSpotify = QLabel(class_name)
	#Set the text of the Spotify label
	class_name.lblSpotify.setText("Spotify Playlist")
	#Set the text alignment for the Spotify label
	class_name.lblSpotify.setAlignment(Qt.AlignCenter)

	#Add the image label for the webcam view to the layout
	layout.addWidget(class_name.image_label, 0, 0)
	#Add the explanation label to the layout
	layout.addWidget(class_name.lblExpl, 0, 1)
	#Add the button to the layout
	layout.addWidget(class_name.contrBtn, 1, 1)
	#Add the Spotify label to the layout
	layout.addWidget(class_name.lblSpotify, 0, 2)

	#Set the GUI to maximed
	class_name.showMaximized()
