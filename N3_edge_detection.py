import cv2
import numpy as np

def N3(INPUT_IMAGE):
    def hysteresis(img, weak, strong=255):
        M, N = img.shape
        for i in range(1, M-1):
            for j in range(1, N-1):
                if (img[i, j] == weak):
                    try:
                        if ((img[i+1, j-1] == strong) or (img[i+1, j] == strong) or (img[i+1, j+1] == strong)
                            or (img[i, j-1] == strong) or (img[i, j+1] == strong)
                                or (img[i-1, j-1] == strong) or (img[i-1, j] == strong) or (img[i-1, j+1] == strong)):
                            img[i, j] = strong
                        else:
                            img[i, j] = 0
                    except IndexError as e:
                        pass
        return img


    def contrast(img, new_max, new_minm):
        row = img.shape[0]
        col = img.shape[1]
        k = 0
        old_minm = np.amin(img)
        old_max = np.amax(img)
        new_img = np.zeros((row, col), dtype=np.uint8)

        for r in range(row):
            for c in range(col):
                new_value = ((new_max-new_minm)/(old_max-old_minm)) * \
                    (img[r, c]-old_minm)+new_minm
                if new_value > 255:
                    new_value = 255
                if new_value < 0:
                    new_value = 0
                new_img[r, c] = new_value
        return new_img


    #########################
    size = 3
    img = cv2.imread(INPUT_IMAGE)
    [row, col] = img.shape[0:2]
    mask = ([1, 1, 1],
         [1, -8, 1],
         [1, 1, 1])
    x = ([0, 0, 0],
        [0, 0, 0],
        [0, 0, 0])

    value = 0

    #############################
    ######### padding#############

    image = np.zeros(((row, col)), dtype=np.uint8)
    bor = int(np.floor(size/2))
    img = np.pad(img, ((bor, bor), (bor, bor), (0, 0)), mode='constant')

    ########### end of paddin#######

    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(gray_image, (3, 3), 1)

    #  smothing using (average)########

    for r in range(row):
        for c in range(col):  # r=0 c=0  sub[0:3,0:0+3] // r=0 c=1 sub [0:3,1:4]
            sub = img_blur[r:r+size, c:c+size]
            res = mask * sub
            value = np.sum(res)
            image[r, c] = value

    ############ show image ###########

    image_norm = hysteresis(image, 0, 255)
    ret, thresh = cv2.threshold(image_norm, 140, 255, cv2.THRESH_BINARY)

    ###### normalize the binary image#######
    final_image = cv2.normalize(thresh, None, 0, 255,
                            cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    edged_image = cv2.Canny(gray_image, threshold1=30, threshold2=100)


    cv2.imshow('edge without normalization', final_image)
    cv2.imshow('original', img)
    cv2.waitKey(0)
    print(final_image)
    print(edged_image)
