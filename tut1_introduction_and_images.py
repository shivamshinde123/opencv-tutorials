import cv2

## reading an image
img = cv2.imread(filename='assets/shivam.JPG', flags=1)

## resizing an image
# img = cv2.resize(img, (400,600))  # way-1 : resize by provided size
img = cv2.resize(img, (0,0), fx=0.1, fy=0.1)  # way - 2 : resize by proportion

## rotating an image
# img = cv2.rotate(img, cv2.ROTATE_180)

# image types that can be loaded
# cv2.IMREAD_COLOR (-1) : loads a color image. Any transparency of image will be neglected. It is the default flag.
# cv2.IMREAD_GRAYSCALE (0): loads an image in grayscale mode
# cv2.IMREAD_UNCHANGED (1): loads an image including alpha channel


## displaying an image
cv2.imshow('ShivamShinde', img)
cv2.waitKey(0)  ## to wait infinitely until I press any key
cv2.destroyAllWindows() ## destroying all the windows that are there so that they won't just suspend on our window


## saving an image
cv2.imwrite('assets/new_image_name.jpg', img)
