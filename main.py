import cv2
from cvzone import findContours
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    _,img=cap.read()
    img1=img
    img= cv2.Canny(img,50,150)
    img= cv2.dilate(img,np.ones((1,1),np.uint8),iterations=1)
    contours, hierarchy=findContours(img1,img)
    cv2.imshow("new",contours)
    cv2.waitKey(1)