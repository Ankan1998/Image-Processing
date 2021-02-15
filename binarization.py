import cv2
import numpy as np



def image_binarization(imageIn, pixel_area = 11, image_constant = 2, Threshold = "adaptive"):
    if len(imageIn.shape) == 3:
        imageIn = cv2.cvtColor(imageIn, cv2.COLOR_BGR2GRAY)
    #imageIn = cv2.cvtColor(imageIn, cv2.COLOR_BGR2GRAY)
    if str(Threshold).lower() == "adaptive":
        thresh = cv2.adaptiveThreshold(imageIn, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,
                                           int(pixel_area), int(image_constant))
        return thresh
    else:
        thresh = cv2.threshold(imageIn, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        return thresh
