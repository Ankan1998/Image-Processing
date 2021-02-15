import cv2
import numpy as np

def erosion_dilation(img):

    kernel = np.ones((2,2), np.uint8)
    erosion = cv2.erode(img, kernel, iterations=1)
    dilation = cv2.dilate(img, kernel, iterations=1)

    return dilation

def dilation_erosion(img):

    kernel = np.ones((2,2), np.uint8)
    dilation = cv2.dilate(img, kernel, iterations=1)
    erosion = cv2.erode(img, kernel, iterations=1)

    return erosion

