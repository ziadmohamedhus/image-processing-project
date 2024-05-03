import cv2
import numpy as np
import matplotlib.pyplot as plt


def histogram(img):

    # Get the dimensions of the image.
    rows, cols = img.shape

    # Get the maximum value in the image.
    mxc = img.max()

    # Create an array to store the histogram.
    counts = np.zeros(mxc + 1, dtype=int)

    # Iterate over the pixels in the image.
    for row in range(rows):
        for col in range(cols):
            v = img[row, col]
            counts[v] += 1

    # Return the histogram.
    return counts

def P8(INPUT_IMAGE):
    img = cv2.imread(INPUT_IMAGE, 0)


    (row, col) = img.shape[0:2]


    count1 = histogram(img)
    bins = list[range(0, 256)]
    plt.hist(count1, bins=10, rwidth=0.9,
         color='#607c8e')
    plt.show()
