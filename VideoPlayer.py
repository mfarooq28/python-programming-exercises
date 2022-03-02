# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 06:56:05 2021

@author: ptcl
"""

import cv2

cap = cv2.VideoCapture("C:\\Users\ptcl\Desktop\\cat.mp4")
print("Cap",cap)

while True:
    ret,frame = cap.read()
    frame = cv2.resize(frame,(350,225))
    gray = cv2.cvtColor(frame,(cv2.COLOR_BGR2GRAY))
    cv2.imshow("frame",frame)
    cv2.imshow("gray",gray)
    k = cv2.waitKey(25)
    if k == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()
