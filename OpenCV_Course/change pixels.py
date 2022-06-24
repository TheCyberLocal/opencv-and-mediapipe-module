import cv2
from random import randint

img = cv2.imread('soccer.png', -1)
# print(img.shape)  # (rows, columns, channels)

# COPY PART OF IMAGE
# 500:700 rows 500 to 700
# 600:900 columns 600 to 900
tag = img[500:700, 600:900]
img[100:300, 700:1000] = tag


for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [randint(0, 255), randint(0, 255), randint(0, 255)]

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
