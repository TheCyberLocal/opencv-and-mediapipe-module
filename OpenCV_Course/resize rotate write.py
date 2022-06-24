import cv2

# READ IMAGE TO IMG
# -1, cv2.IMREAD_COLOR
# 0, cv2.IMREAD_GRAYSCALE
# 1, cv2.IMREAD_UNCHANGED
img = cv2.imread('soccer.png', -1)
# img = cv2.resize(img, (1080, 720))
img = cv2.resize(img, (0, 0), fx=0.3, fy=0.3)

# ROTATE IMAGE
# img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
# img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
img = cv2.rotate(img, cv2.ROTATE_180)

# WRITE IMG TO IMAGE
cv2.imwrite('new_soccer.png', img)

# SHOW IMG
cv2.imshow('Image', img)

# WAIT FOR ANY KEY TO CONTINUE
cv2.waitKey(0)

# CLOSE ALL WINDOWS
cv2.destroyAllWindows()
