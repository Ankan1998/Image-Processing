import cv2 

def brightness_and_contrast(image,parameter=0.24):
    if parameter=="":
        parameter=0.24
    imageIn = cv2.imread(image)
    invGamma = 1.0 / float(parameter)
    table = np.array([((i / 255.0) ** invGamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")
    imageOut = cv2.LUT(imageIn, table)
    cv2.imwrite(image,imageOut)
    return image