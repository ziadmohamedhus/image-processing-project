import cv2
import numpy as np
import math

def P3(INPUT_IMAGE,x):
    # reading image
    img=cv2.imread(INPUT_IMAGE)
    row=img.shape[0]
    col=img.shape[1]
    ch=img.shape[2]
    offset=x
    k=0
    r=0
    c=0
    new_img=np.zeros((row,col,ch),dtype=np.uint8)

    for k in range(ch):
        for r in range(row):
            for c in range(col):
                new_value=img[r,c,k]+offset
                if new_value>255:
                    new_value=255
                if new_value<0:
                    new_value=0
                new_img[r,c,k]=new_value


    cv2.imshow("before",img)
    cv2.imshow("after",new_img)
    cv2.waitKey(0)
