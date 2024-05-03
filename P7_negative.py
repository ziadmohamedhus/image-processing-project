import cv2
import numpy as np
import math

def P7(INPUT_IMAGE):
    # reading image
    img=cv2.imread(INPUT_IMAGE)
    (row,col,ch)=img.shape[0:3]
    new_img=np.zeros((row,col,ch),dtype=np.uint8)

    for k in range(ch):
        for r in range(row):
            for c in range(col):
                new_value=255-img[r,c,k]
                new_img[r,c,k]=new_value


    cv2.imshow("before",img)
    cv2.imshow("after",new_img)
    cv2.waitKey(0)
