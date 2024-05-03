import cv2
import numpy as np
def P6(INPUT_IMAGE):
    img = cv2.imread(INPUT_IMAGE)
    row, col, ch = img.shape
    img = np.asarray(img, dtype=np.double)

    new_image = np.zeros((row, col, ch), dtype=np.uint8)

    levels = 2**8
    gap = 256 / levels

    for k in range(ch):
        for r in range(row):
            for c in range(col):
                temp = img[r, c] / gap
                index = np.floor(temp)
                color = (index - 5) * gap
                new_image[r, c] = color

    cv2.imshow('image', new_image)
    cv2.waitKey(0)

