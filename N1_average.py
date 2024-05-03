
import cv2 
import numpy as np

def N1(INPUT_IMAGE):
    ############### reading an image and mask #################
    ###########################################################
    img=cv2.imread(INPUT_IMAGE)
    [row,col,ch]=img.shape[0:3]
    mask=([1/9,1/9,1/9],
                [1/9,1/9,1/9],
                [1/9,1/9,1/9])
    x=(           [0,0,0],
                [0,0,0],
                [0,0,0])
    size=3
    value=0

    ################## start of padding ######################
    #########################################################
    image =np.zeros(((row,col,ch)),dtype=np.uint8)
    bor=int(np.floor(size/2))
    img=np.pad(img ,((bor,bor),(bor,bor),(0,0)),mode='constant')

    ################### end of padding########################
    ##########################################################


    ################ appling mask on image ####################
    ###########################################################

    for k in range(ch):
        for r in range(row):
            for c in range(col): # r=0 c=0  sub[0:3,0:0+3] // r=0 c=1 sub [0:3,1:4]
                sub =img[r:r+size,c:c+size,k]
                res= mask * sub
                value=np.sum(res)
                image[r,c,k]=value

    ################# show image #########################
    ######################################################
    cv2.imshow('smoothing(average)',image)
    cv2.imshow('original',img)
    cv2.waitKey(0)
