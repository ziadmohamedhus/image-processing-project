import matplotlib.pyplot as plt
import cv2
from skimage import data
from skimage import exposure
from skimage.exposure import match_histograms
def P11(IMAGE1,IMAGE2):
    reference = cv2.imread(IMAGE1)
    image = cv2.imread(IMAGE2)

    matched = match_histograms(image, reference, channel_axis=-1)

    fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(8, 3),
                                    sharex=True, sharey=True)
    for aa in (ax1, ax2, ax3):
        aa.set_axis_off()

    ax1.imshow(image)
    ax1.set_title('Source')
    ax2.imshow(reference)
    ax2.set_title('Reference')
    ax3.imshow(matched)
    ax3.set_title('Matched')

    plt.tight_layout()
    plt.show()
