import numpy as np
import cv2

img = cv2.imread('soccer.png')
img = cv2.resize(img, (0, 0), fx=0.3, fy=0.3)
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

maximum_corners, confidence = 100, 0.6
# minimum distance between two corners for it not to be considered one
minimum_dis = 10
corners = cv2.goodFeaturesToTrack(grey, maximum_corners, confidence, minimum_dis)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, (color), 1)

cv2.imshow('frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
