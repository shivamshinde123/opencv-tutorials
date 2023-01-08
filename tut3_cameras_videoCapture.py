import numpy as np
import cv2

## accessing a webcam from the laptop
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() 

    ## getting the width and height of the video capture
    width = int(cap.get(3))
    height = int(cap.get(4))

    # here ret will tell us if the video image capture was success or failure
    # frame will return a frame image

    ## creating a placeholder array for our image
    image = np.zeros(frame.shape, np.uint8)

    ## resizing a frame to its quarter size
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)

    ## placing the smaller_frame after some preprocessing in four quadrants of the image
    image[:height//2, :width//2] = smaller_frame
    image[:height//2, (width//2):] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[(height//2):, :width//2] = smaller_frame
    image[(height//2):, (width//2):] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    
    ## showing the image after all these operations. we should see four image of ourself.
    cv2.imshow('frame', image)

    # this will check if the key you pressed on keyboard is 'q' or not.
    # and if you have pressed a 'q' key, then the webcam will be closed
    if cv2.waitKey(1) == ord('q'): 
        break


## releasing the webcam camera so that other resources can use it
cap.release()
cv2.destroyAllWindows()