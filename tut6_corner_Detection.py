import cv2
import numpy as np

img = cv2.imread('assets/shivam.JPG')
img = cv2.resize(img, (0,0), fx=0.05, fy=0.05)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


corners = cv2.goodFeaturesToTrack(gray, maxCorners=1000, qualityLevel=0.01, minDistance=10)

## here we get the corner coordinates as a floating point numbers
## since we will be using those coordinates to draw the circles, we will convert the coordinates into the integer
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x,y), radius=1, color=(255,0,0))

## drawing the lines between every two points for fun.
# for i in range(len(corners)):
#     for j in range(i + 1, len(corners)):
#         corner1 = tuple(corners[i][0])
#         corner2 = tuple(corners[j][0])
#         color = tuple(map(lambda x: int(x), np.random.randint(0,255, size=3)))
#         cv2.line(img, corner1, corner2, color=color, thickness=1)

cv2.imshow('frame',img)


cv2.waitKey(0)
cv2.destroyAllWindows()