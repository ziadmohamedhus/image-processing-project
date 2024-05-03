import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
def F5(INPUT_IMAGE,x):
    # original image
    f = cv2.imread(INPUT_IMAGE, 0)

    plt.imshow(f, cmap='gray')
    plt.axis('off')
    plt.show()

    # image in frequency domain
    F = np.fft.fft2(f)


    Fshift = np.fft.fftshift(F)


    # Filter: High pass filter
    M, N = f.shape
    H = np.zeros((M, N), dtype=np.float32)
    D0 = x

    for u in range(M):
        for v in range(N):
            D = np.sqrt((u-M/2)**2 + (v-N/2)**2)
            H[u, v] = np.exp(-D**2/(2*D0*D0))


    # Ideal High Pass Filtering
    Gshift = Fshift * H


    # Inverse Fourier Transform
    G = np.fft.ifftshift(Gshift)


    g = np.abs(np.fft.ifft2(G))
    plt.imshow(g, cmap='gray')
    plt.axis('off')
    plt.show()
