import cv2
import numpy as np
import math

def P5(INPUT_IMAGE,x):
    # Load the image
    img = cv2.imread(INPUT_IMAGE)
    # Apply Gamma=2.2 on the normalised image and then multiply by scaling constant (For 8 bit, c=255)
    image_1 = np.array(255*(img/255)**x, dtype='uint8')
    
    # Display the images in subplots
    cv2.imshow('after', image_1)
    cv2.waitKey(0)