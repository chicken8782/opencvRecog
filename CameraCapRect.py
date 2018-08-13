# -*- coding: utf-8 -*-
import numpy as np
import cv2
import os

#cascade file
cascade_file = "haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(cascade_file)

cap = cv2.VideoCapture(0)
color = (255, 255, 255)# white

while(True):
 # フレームをキャプチャする
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
    # エッジ検出

 frame = cv2.Canny(frame,100,200)

    # 画面に表示する
 cv2.imshow('frame',frame)

 # キーボード入力待ち
 key = cv2.waitKey(1) & 0xFF

 # qが押された場合は終了する
 if key == ord('q'):
  break
 # sが押された場合は保存する
 if key == ord('s'):
  path = "photo.jpg"
  cv2.imwrite(path,frame)



# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
