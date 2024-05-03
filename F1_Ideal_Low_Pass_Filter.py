import cv2
import numpy as np
import matplotlib.pyplot as plt
def F1(INPUT_IMAGE,x):
    # original image
    f = cv2.imread(INPUT_IMAGE, 0)

    plt.imshow(f, cmap='gray')
    plt.axis('off')
    plt.show()

    # image in frequency domain
    F = np.fft.fft2(f)


    Fshift = np.fft.fftshift(F)


    # Filter: Low pass filter
    M, N = f.shape
    H = np.zeros((M, N), dtype=np.float32)
    D0 = x
    for u in range(M):
        for v in range(N):
            D = np.sqrt((u-M/2)**2 + (v-N/2)**2)
            if D <= D0:
                H[u, v] = 1
            else:
                H[u, v] = 0


    # Ideal low Pass Filtering
    Gshift = Fshift * H


    # Inverse Fourier Transform
    G = np.fft.ifftshift(Gshift)


    g = np.abs(np.fft.ifft2(G))
    plt.imshow(g, cmap='gray')
    plt.axis('off')
    plt.show()
