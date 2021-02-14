import os
from pdf2image import convert_from_path
import cv2
import numpy as np

def single_image_converter(filename):
    img = convert_from_path(filename, 300)[0]
    img=np.array(img)
    return img

# def folder_image_converter(dir):
#     for file in os.listdir(os.getcwd(),dir):
#
# path="5_20010184281.pdf"
#
# plt.imshow(img)
# plt.show()
# img_= np.array(img)
# cv2.imwrite("2.jpg",img_)
