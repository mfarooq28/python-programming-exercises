# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 18:44:19 2021

@author: ptcl
"""

import cv2
img1 = cv2.imread("C:\\Users\ptcl\Pictures\\avengers.jpg", 1)
img1 = cv2.resize(img1,(640,350))
img1 = cv2.flip(img1,(0))
print(img1)
cv2.imshow("Original", img1)


img2 = cv2.imread("C:\\Users\ptcl\Pictures\\avengers.jpg", 0)
img2 = cv2.resize(img2,(640,350))
print(img2)

img3 = cv2.imread("C:\\Users\ptcl\Pictures\\avengers.jpg", -1)
img3 = cv2.resize(img3,(640,350))
print(img3)
cv2.imshow("Unchanged", img3)


cv2.imshow("GrayScale", img2)
cv2.imwrite("C:\\Users\ptcl\Pictures\\AvengersGrayScale.jpg", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()