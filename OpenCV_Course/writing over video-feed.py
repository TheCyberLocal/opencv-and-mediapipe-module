import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame, (0, 0), (width, height), (0, 255, 0), 10)
    img = cv2.line(img, (0, int(height/2)), (width, int(height/2)), (0, 0, 255), 10)

    img = cv2.rectangle(img, (100, 100), (300, 200), (255, 0, 0), 10)

    img = cv2.circle(img, (200, 400), 60, (0, 0, 255), -1)  # use -1 for thicknees to fill shape

    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    text = """I learned how to write over videofeed"""
    img = cv2.putText(img, text, (10, 50), font, fontScale, (0, 100, 100), 2, cv2.LINE_AA)

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
