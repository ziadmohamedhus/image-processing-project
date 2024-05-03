import cv2 
import numpy as np
def N4(INPUT_IMAGE):
    size=3
    img=cv2.imread(INPUT_IMAGE)
    [row,col,ch]=img.shape[0:3]
    mask=([0,-1,0],
                [-1,5,-1],
                [0,-1,0])
    x=(             [0,0,0],
                [0,0,0],
                [0,0,0])

    value=0
    # padding ---

    image =np.zeros(((row,col,ch)),dtype=np.uint8)
    bor=int(np.floor(size/2))
    img=np.pad(img ,((bor,bor),(bor,bor),(0,0)),mode='constant')
    # end of padding

    #  smothing using (average)
    for k in range(ch):
        for r in range(row):
            for c in range(col): # r=0 c=0  sub[0:3,0:0+3] // r=0 c=1 sub [0:3,1:4]
                sub =img[r:r+size,c:c+size,k]
                res= mask * sub
                value=np.sum(res)
                if (value<0):
                    value=0
                if(value>255):
                    value=255
                image[r,c,k]=value

    cv2.imshow('sharpining',image)
    cv2.imshow('original',img)
    cv2.waitKey(0)
