import cv2
import numpy as np
def N5(INPUT_IMAGE):
    def gaussian_kernel(size, sigma=1):
        size = int(size) // 2
        x, y = np.mgrid[-size:size+1, -size:size+1]
        normal = 1 / (2.0 * np.pi * sigma**2)
        g =  np.exp(-((x**2 + y**2) / (2.0*sigma**2))) * normal
        return g

    size=3
    value=0
    img=cv2.imread(INPUT_IMAGE)
    [row,col,ch]=img.shape[0:3]
    mask=gaussian_kernel(size,1)

    # padding ---

    image =np.zeros(((row,col,ch)),dtype=np.uint8)
    bor=int(np.floor(size/2))
    img=np.pad(img ,((bor,bor),(bor,bor),(0,0)),mode='constant')
    # end of padding

    #  smothing using (weighted)
    for k in range(ch):
        for r in range(row):
            for c in range(col): # r=0 c=0  sub[0:3,0:0+3] // r=0 c=1 sub [0:3,1:4]
                sub =img[r:r+size,c:c+size,k]
                res= mask * sub
                value=np.sum(res)
                image[r,c,k]=value

    [row2,col2,ch2]=image.shape[0:3]

    image_resized=cv2.resize(img,dsize=[col2,row2])

    image_sub=cv2.subtract(image_resized,image)
    image_add=cv2.add(image_sub,image_resized)

    cv2.imshow('unsharp',image_add)
    cv2.imshow('original',img)
    cv2.waitKey(0)