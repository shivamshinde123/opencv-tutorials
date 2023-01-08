import cv2
import random

img = cv2.imread('assets/shivam3.JPG', -1)
img = cv2.resize(img, (0,0), fx=0.1, fy=0.1)

## opencv stores images as a numpy array
## so we can use the numpy methods on the img object such as shape

# print(img)
# print(img.shape)  # this will give us shape in the format (height, width, channel) i.e, (rows, columns, channels)

## also opencv uses the format of BLUE, GREEN , RED (BGR)

## replacing some part of image with random pixel values for fun
for i in range(img.shape[0]):
    for j in range(50):
        img[i][j] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]



cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()