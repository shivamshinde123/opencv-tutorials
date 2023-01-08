import cv2
import numpy as np

img = cv2.imread('assets/shivam.JPG', 0)
img = cv2.resize(img, (0,0), fx=0.1, fy=0.1)

## we get the better results for template matching when the template image
## has the similar size as that of an object we are supposed to find in the
## original image

template = cv2.imread('assets/shivam_feta.png', 0)

h, w = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:

    img2 = img.copy()

    ## following code block will basically convolve the template image over
    ## the original image and find the place where we will find the closet match
    ## this will return an array of size (h - f1 + 1) x (w - f2 + 1)
    ## where, h and w are the dimensions of the original image and f1xf2 are the dimension of the template image
    result = cv2.matchTemplate(img, template,method)

    ## depending on the methods, minimum value location or maximum value location will 
    ## give us the position of the template image in the original image
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    ## drawing the rectable using the min_loc and max_loc
    ## some of the methods use the minimum location for the match and some use the maximum value for the match
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    ## location will be the top-left point on our rectangle
    ## now, we need to find the bottom-right point to create our rectangle

    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, pt1=location, pt2=bottom_right, color=(255,0,0), thickness=5 )
    cv2.imshow('MATCH', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
