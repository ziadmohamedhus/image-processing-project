
import cv2
import numpy as np


def direct_mapping_order_1(old_img, fact):
    # Get the dimensions of the old image.
    old_rows, old_cols, channels = old_img.shape
    print(old_rows)
    print(old_cols)
    # Create a new image that is the size of the old image
    new_rows = old_rows * fact
    new_cols = old_cols * fact
    print(new_cols)
    print(new_rows)
    new_img = np.zeros((new_rows, new_cols, channels), dtype=np.uint8)

    # Copy the old image to the new image.
    for ch in range(channels):
        for row in range(old_rows):
            for col in range(old_cols):
                new_img[row * fact, col * fact, ch] = old_img[row, col, ch]

    for ch in range(channels):
        for row in range(0, new_rows, fact):
            for start in range(0, new_cols - fact, fact):
                x = new_img[row, start, ch]
                y = new_img[row, start + fact, ch]
                l = start + 1
                r = start + fact
                if x == y:
                    new_img[row, l:r, ch] = x
                else:
                    it = 0
                    if x < y:
                        for col in range(l, r):
                            it += 1
                            new_img[row, col, ch] = round(
                                ((y - x) / fact) * it + x)
                    else:
                        for col in range(r, l - 1, -1):
                            it += 1
                            new_img[row, col, ch] = round(
                                ((x - y) / fact) * it + y)

    for ch in range(channels):
        for col in range(0, new_cols - fact + 1):
            for start in range(0, new_rows - fact, fact):
                x = new_img[start, col, ch]
                y = new_img[start + fact, col, ch]
                u = start + 1
                d = start + fact
                if x == y:
                    new_img[u:d, col, ch] = x
                else:
                    it = 0
                    if x < y:
                        for row in range(u, d):
                            it += 1
                            new_img[row, col, ch] = round(
                                ((y - x) / fact) * it + x)
                    else:
                        for row in range(d, u - 1, -1):
                            it += 1
                            new_img[row, col, ch] = round(
                                ((x - y) / fact) * it + y)
    for ch in range(channels):
        for row in range(1, new_rows - fact + 1):
            new_img[row, new_cols - fact + 2:new_cols,
                    ch] = new_img[row, new_cols - fact + 1, ch]

    for ch in range(channels):
        for row in range(new_rows - fact + 2, new_rows):
            new_img[row, :, ch] = new_img[new_rows - fact + 1, :, ch]
    return new_img

def DM1(INPUT_IMAGE,x):
    img = cv2.imread(INPUT_IMAGE)

    resized_image = direct_mapping_order_1(img, x)
    cv2.imshow('image', resized_image)
    cv2.waitKey(0)
    print(resized_image)

