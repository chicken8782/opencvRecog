# -*- coding: utf-8 -*-

import cv2
#HAAR分類器の顔検出用の特徴量
cascade_path = "haarcascade_frontalface_alt.xml"

image_path = "lena_std.jpg"

color = (255, 255, 255) #白
#image読み込み
image = cv2.imread(image_path)
#グレースケール変換
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#カスケード分類機の特徴を取得
cascade = cv2.CascadeClassifier(cascade_path)

facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))
print ("face rectangle")
print (facerect)

if len (facerect) > 0:
    #検出した顔を囲む矩形の作成
    for rect in facerect:
        cv2.rectangle(image, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), color, thickness = 2)

    cv2.imwrite("detected.jpg", image)
