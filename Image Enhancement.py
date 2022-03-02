# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 19:00:30 2021

@author: ptcl
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("C:\\Users\ptcl\Documents\Python Scripts\\IIUI.jpg")

#plt.figure(figsize=(20,8))
#plt.imshow(img)

img = cv2.resize(img,(640,320))
#img1 = cv2.flip(img,(0))
print(img)
cv2.imshow("Original", img)

cv2.waitKey(0)
cv2.destroyAllWindows()