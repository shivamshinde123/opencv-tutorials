import numpy as np
import cv2

## accessing a webcam from the laptop
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() 

    ## getting the width and height of the video capture
    width = int(cap.get(3))
    height = int(cap.get(4))

   
    ## showing the image after all these operations. we should see four image of ourself.
    cv2.imshow('frame', frame)

    # this will check if the key you pressed on keyboard is 'q' or not.
    # and if you have pressed a 'q' key, then the webcam will be closed
    if cv2.waitKey(1) == ord('q'): 
        break


## releasing the webcam camera so that other resources can use it
cap.release()
cv2.destroyAllWindows()