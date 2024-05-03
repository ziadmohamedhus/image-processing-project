
import cv2
import numpy as np


def direct_mapping_order_0(old_img, fact):

    # Get the dimensions of the image.
    old_rows, old_cols, channels = old_img.shape

    # Create a new image with the upsampled dimensions.
    new_rows = old_rows * fact
    new_cols = old_cols * fact
    new_img = np.zeros((new_rows, new_cols, channels), dtype=old_img.dtype)

    # Iterate over the pixels.
    for ch in range(channels):
        for row in range(old_rows):
            for col in range(old_cols):
                new_img[(row - 1) * fact:row * fact, (col - 1) *
                        fact:col * fact, ch] = old_img[row, col, ch]

    # Convert the image to 8-bit unsigned integer.
    new_img = np.uint8(new_img)

    # Return the upsampled image.
    return new_img

def DM0(INPUT_IMAGE,x):
    img = cv2.imread(INPUT_IMAGE)
    final = direct_mapping_order_0(img, x)
    cv2.imshow('image', final)
    cv2.waitKey(0)
