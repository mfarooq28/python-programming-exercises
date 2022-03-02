# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 07:37:42 2021

@author: ptcl
"""

import cv2

cap = cv2.VideoCapture(0)
print(cap)

while cap.isOpened():
    ret,frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame,(350,225))
        gray = cv2.cvtColor(frame,(cv2.COLOR_BGR2GRAY))
        cv2.imshow("frame",frame)
        cv2.imshow("gray",gray)
        k = cv2.waitKey(1)
        if k == ord("q"):
            break
    
cap.release()
cv2.destroyAllWindows()