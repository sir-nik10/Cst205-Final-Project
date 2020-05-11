import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)

while True:
	# read frame by frame
	ret, frame = cap.read()
	# Flip the cameraa
	# convert what it's reading into gray, not what we see
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)

	for(x, y, w, h) in faces:
		print(x,y,w,h)
		roi_gray = gray[y:y+h, x:x+w] #(ycord_start, ycord_end)
		roi_color = frame[y:y+h, x:x+w]

		# if you want to save a snapshot of face
		#img_item = "my_img.png"
		#cv2.imwrit(img_item, roi_gray)

		#Create a box around face
		color = (255, 0, 0) # BGR values
		stroke = 2
		end_cord_x = x + w
		end_cord_y = y + h
		cv2.rectangle(frame, (x,y), (end_cord_x, end_cord_y), color, stroke)


	cv2.imshow('frame', frame)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break
cap.release()
cv2.destryAllWindows()