from torch_snippets import *
import selectivesearch
# from skimage.segmentation import felzenszwalb
import numpy as np

def extract_region(img):   
    _,regions = selectivesearch.selective_search(img)
    # img.shape[0]*img_shape[1]
    img_area = np.prod(img.shape[:2])  
    cor_region = []
    for i in regions:
        if i['rect'] in cor_region:
            continue
        if i['size'] < 0.05*img_area:
            continue
        if i['size'] > img_area:
            continue
        x,y,w,h = i['rect']
        cor_region.append(list(i['rect']))
    
    return cor_region

if __name__ == '__main__':
    img = read(r'C:\Users\Ankan\Desktop\Github\Image-Processing\Images\bird_c.png',1)
    regions = extract_region(img)
    show(img, bbs=regions)
    
