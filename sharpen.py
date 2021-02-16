import cv2
import numpy as np

def sharpen_(imageIn):

    filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    # Applying cv2.filter2D function on our Cybertruck image
    sharpen_img = cv2.filter2D(imageIn,-1,filter)

    return sharpen_img