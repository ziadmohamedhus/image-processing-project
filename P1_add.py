import cv2
import numpy as np

import numpy as np


def add_images(img1, img2):
    """
    This function adds two images.

    Args:
      img1: The first image.
      img2: The second image.

    Returns:
      The sum of the two images.
    """

    # Check if the images have the same dimensions.
    if img1.shape != img2.shape:
        raise ValueError("The images must have the same dimensions.")

    # Add the two images.
    new_img = img1 + img2

    # Return the new image.
    return new_img


'''
def addImgs(img1, img2):
    # Get the shapes of the images.
    rows1, cols1, chns = img1.shape
    rows2, cols2, _ = img2.shape
    min_rows = min(rows1, rows2)
    min_cols = min(cols1, cols2)
    new_img = np.zeros((min_rows, min_cols, chns), dtype=np.uint8)
    for chn in range(chns):
        for row in range(min_rows):
            for col in range(min_cols):
                new_img[row, col, chn] = img1[row,
                                              col, chn] + img2[row, col, chn]

    return new_img

'''

def P1(IMAGE1,IMAGE2):
    img1 = cv2.imread(IMAGE1)
    img2 = cv2.imread(IMAGE2)
    
    final = add_images(img1, img2)
    cv2.imshow('image', final)
    cv2.waitKey(0)
