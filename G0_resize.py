

import cv2
import numpy as np

def G0(image,x,y):
    img = cv2.imread(image)
    c=(x,y)
    img=cv2.resize(img,c)
    cv2.imshow('after',img)
