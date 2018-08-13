# -*- coding: utf-8 -*-
import cv2
import os
#cascade file
cascade_file = "haarcascade_frontalface_alt.xml"
#get feature point
cascade = cv2.CascadeClassifier(cascade_file)
#Capture from cam
cap = cv2.VideoCapture(0)
color = (255, 255, 255)# white
while(True):
    #get frame from video stream
    ret, frame = cap.read()
    #face recognition
    facerect = cascade.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=2, minSize=(10, 10))

     for rect in facerect:
        # put rectangle
        cv2.rectangle(frame, tuple(rect[0:2]),tuple(rect[0:2] + rect[2:4]), color, thickness=2)

     # show
    cv2.imshow("Show FLAME Image", frame)

    # end after 'q' pressed
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

    cap.release()
    cv2.destroyAllWindows()
