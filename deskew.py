import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Calculate skew angle of an image
def getSkewAngle(cvImage):
    # Prep image, copy, convert to gray scale, blur, and threshold
    newImage = cvImage.copy()
    #shape=newImage.shape
    if len(newImage.shape) == 3:
        gray = cv2.cvtColor(newImage, cv2.COLOR_BGR2GRAY)
    else:
        gray = newImage
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Apply dilate to merge text into meaningful lines/paragraphs.
    # Use larger kernel on X axis to merge characters into single line, cancelling out any spaces.
    # But use smaller kernel on Y axis to separate between different blocks of text
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 5))
    dilate = cv2.dilate(thresh, kernel, iterations=5)

    # Find all contours
    contours, hierarchy = cv2.findContours(dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key = cv2.contourArea, reverse = True)

    # allContourAngles = [cv2.minAreaRect(c)[-1] for c in contours]
    # angle = sum(allContourAngles) / len(allContourAngles)

    middleContour = contours[len(contours) // 2]
    angle = cv2.minAreaRect(middleContour)[-1]

    # largestContour = contours[0]
    # middleContour = contours[len(contours) // 2]
    # smallestContour = contours[-1]
    # angle = sum([cv2.minAreaRect(largestContour)[-1], cv2.minAreaRect(middleContour)[-1],cv2.minAreaRect(smallestContour)[-1]]) / 3

    # Find largest contour and surround in min area box
    #largestContour = contours[0]
    #minAreaRect = cv2.minAreaRect(largestContour)

    # Determine the angle. Convert it to the value that was originally used to obtain skewed image
    #angle = minAreaRect[-1]
    if angle < -45:
        angle = 90 + angle
    return -1.0 * angle



# Rotate the image around its center
def rotateImage(cvImage, angle: float):
    newImage = cvImage.copy()
    (h, w) = newImage.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    newImage = cv2.warpAffine(newImage, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return newImage

# Deskew image
def deskew(cvImage):
    angle = getSkewAngle(cvImage)
    return rotateImage(cvImage, -1.0 * angle)



# f=r"2.jpg"
# img=Image.open(f)
# img=np.array(img)
# rot_img=deskew(img)
# cv2.imwrite("rot.jpg",rot_img)


