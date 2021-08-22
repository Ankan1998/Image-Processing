import cv2
import numpy as np
import os
def get_text_objects(filedir,output_dir):
    for filename in os.listdir(filedir):
        original_filename = os.path.splitext(os.path.basename(filename))[0]
        ext= os.path.splitext(os.path.basename(filename))[1]
        filename=filedir+"/"+filename
        img = cv2.imread(filename)
        #print("image_shape", img.shape)
        orig_h,orig_w= img.shape[:2]
        mser = cv2.MSER_create()
        img = cv2.resize(img, (img.shape[1]*2, img.shape[0]*2))
        #print("resized_image_shape",img.shape)
        h,w,c = img.shape
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        vis = img.copy()

        new_image= np.zeros([h,w,c],dtype=np.uint8)
        new_image.fill(255)
        #print("new_image_shape", new_image.shape)

        regions = mser.detectRegions(gray)
        hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions[0]]
        cv2.polylines(vis, hulls, 1, (0,255,0))
        #contours = sorted(hulls, key=lambda ctr: cv2.boundingRect(ctr)[0])
        for hull in hulls:
            x,y,w,h = cv2.boundingRect(hull)
            #print("x,y,w,h",x,y,w,h)
            #print(img.shape,new_image.shape)
            crop_image = img[y:y+h,x:x+w]
            # cv2.imshow('crop_image', crop_image)
            # cv2.waitKey()
            # cv2.destroyAllWindows()
            new_image[y:y+h,x:x+w]=crop_image
            #cv2.drawContours(new_image, [hull], -1, (0, 0, 0), -1)
        # vis = vis[5:-5, 5:-5, :]
        # cv2.namedWindow('img', 0)
        # cv2.imshow('img', vis)
        # while(cv2.waitKey()!=ord('q')):
        #     continue
        # cv2.destroyAllWindows()
        new_image= cv2.resize(new_image,(orig_w,orig_h))
        #print(new_image.shape)
        cv2.imwrite(os.path.join(output_dir,original_filename+ext),new_image)