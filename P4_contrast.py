import cv2
import numpy as np
import math

def P4(INPUT_IMAGE,x,y):
    # reading image
    img=cv2.imread(INPUT_IMAGE)
    def contrast (img,new_max,new_minm):
        row=img.shape[0]
        col=img.shape[1]
        ch=img.shape[2]
        k=0
        old_minm=np.amin(img)
        old_max=np.amax(img)
        new_img=np.zeros((row,col,ch),dtype=np.uint8)

        for k in range(ch):
            for r in range(row):
                for c in range(col):
                    new_value=((new_max-new_minm)/(old_max-old_minm))*(img[r,c,k]-old_minm)+new_minm
                    if new_value>255:
                        new_value=255
                    if new_value<0:
                        new_value=0
                    new_img[r,c,k]=new_value
        return new_img

    new_img=contrast(img,x,y)
    cv2.imshow("before",img)
    cv2.imshow("after",new_img)
    cv2.waitKey(0)


