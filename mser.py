import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def mser_(img):

    orig_h, orig_w = img.shape[:2]
    mser = cv2.MSER_create()
    img = cv2.resize(img, (img.shape[1] * 2, img.shape[0] * 2))
    # print("resized_image_shape",img.shape)
    #if len(img.shape)==2:

    h, w = img.shape[0],img.shape[1]
    if len(img.shape) == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img
    vis = img.copy()

    new_image = np.zeros([h, w], dtype=np.uint8)
    new_image.fill(255)
    # print("new_image_shape", new_image.shape)

    regions = mser.detectRegions(gray)
    hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions[0]]
    cv2.polylines(vis, hulls, 1, (0, 255, 0))
    # contours = sorted(hulls, key=lambda ctr: cv2.boundingRect(ctr)[0])
    for hull in hulls:
        x, y, w, h = cv2.boundingRect(hull)
        # print("x,y,w,h",x,y,w,h)
        # print(img.shape,new_image.shape)
        crop_image = img[y:y + h, x:x + w]
        # cv2.imshow('crop_image', crop_image)
        # cv2.waitKey()
        # cv2.destroyAllWindows()
        new_image[y:y + h, x:x + w] = crop_image

    return new_image

if __name__=="__main__":
    filename=r"C:\Users\Ankan\Desktop\Invoice_image_processing\img_dir\2074824672.jpg"
    img = Image.open(filename)

    img = np.array(img)
    plt.imshow(img)
    plt.show()
    #img = cv2.cvtColor()
    img = mser_(img)
    plt.imshow(img)
    plt.show()