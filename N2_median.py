import cv2
import numpy as np
from numpy import median

def N2(INPUT_IMAGE):
    size = 3
    value = 0
    img = cv2.imread(INPUT_IMAGE)
    [row, col, ch] = img.shape[0:3]

    ####################### padding###############
    #############################################

    image = np.zeros(((row, col, ch)), dtype=np.uint8)
    bor = int(np.floor(size/2))
    img = np.pad(img, ((bor, bor), (bor, bor), (0, 0)), mode='constant')

    ##################### end of padding##########
    ##############################################

    ############# smothing using (weighted)#######
    for k in range(ch):
        for r in range(row):
            # r=0 c=0  sub[0:3,0:0+3] // r=0 c=1 sub [0:3,1:4]
            for c in range(col):
                sub = img[r:r+size, c:c+size, k]
                value = median(sub)
                image[r, c, k] = value

    ################## show an image #############
    cv2.imshow('smoothing', image)
    cv2.imshow('original', img)
    cv2.waitKey(0)
