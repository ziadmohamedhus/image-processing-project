import cv2
import numpy as np
import math

def P10(INPUT):
    # reading image
    img=cv2.imread(INPUT)


    (row, col) = img.shape[0:2]

    for i in range(row):
        for j in range(col):
        
            img[i, j] = sum(img[i, j]) / 3
  
    cv2.imshow('Grayscale Image', img)
    cv2.waitKey(0)





