import cv2

def remove_noise(self, imageIn, filter):
    #image = cv2.imread(imageIn)
    if filter == "":
        filter = "remove_noise_keeping_edges"
    if filter.lower() == "edge_and_object":
        blur = cv2.GaussianBlur(imageIn, (11, 11), 0)
        blur = cv2.medianBlur(blur, 9)
        return blur
        #cv2.imwrite(imageIn, blur)
    elif filter.lower() == "edge":
        blur = cv2.GaussianBlur(imageIn, (9, 9), 0)
        return blur
        #cv2.imwrite(imageIn, blur)
    elif filter.lower() == "edge_and_surrounding":
        blur = cv2.GaussianBlur(imageIn, (11, 11), 0)
        return blur
        #cv2.imwrite(imageIn, blur)
    elif filter.lower() == "object":
        blur = cv2.medianBlur(imageIn, 9)
        return blur
        #cv2.imwrite(imageIn, blur)
    elif filter.lower() == "remove_noise_keeping_edges":
        blur = cv2.bilateralFilter(imageIn, 9, 25, 50)
        return blur
        #cv2.imwrite(imageIn, blur)

    elif filter.lower() == "minimum":
        blur = cv2.blur(imageIn, (5, 5))
        return blur
        #cv2.imwrite(imageIn, blur)