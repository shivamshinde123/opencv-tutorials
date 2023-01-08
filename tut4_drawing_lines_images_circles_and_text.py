import cv2


import numpy as np
import cv2

## accessing a webcam from the laptop
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() 

    ## getting the width and height of the video capture
    width = int(cap.get(3))
    height = int(cap.get(4))

    ## note that in opencv, the coordinate for the origin is placed at upper left corner of the image
    ## as we go to the right side, x value increases
    ## as we go to the bottom side, y value increases
    img = cv2.line(frame, pt1=(0,0), pt2=(width, height), color=(255,0,0),thickness=10)
    img = cv2.line(img, pt1=(width,0), pt2=(0, height), color=(0,255,0),thickness=10)
    img = cv2.rectangle(img, pt1=(100,200), pt2=(150,350), color=(187,38,200),thickness=10)
    img = cv2.circle(img, center=(300,300), radius=50, color=(10,10,100), thickness=5)

    font = cv2.FONT_HERSHEY_COMPLEX
    img = cv2.putText(img, 'Shivam Shinde', org=(200, height-10),fontFace=font, thickness=3, lineType=cv2.LINE_AA, fontScale=1,color=(12,100,0))


    ## showing the image after all these operations. we should see four image of ourself.
    cv2.imshow('frame', img)

    # this will check if the key you pressed on keyboard is 'q' or not.
    # and if you have pressed a 'q' key, then the webcam will be closed
    if cv2.waitKey(1) == ord('q'): 
        break


## releasing the webcam camera so that other resources can use it
cap.release()
cv2.destroyAllWindows()