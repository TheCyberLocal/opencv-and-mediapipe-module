import cv2

cap = cv2.VideoCapture(0)
combos = ['rgb', 'rg', 'rb', 'gb', 'r', 'g', 'b']
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    for x in combos:
        k = frame.copy()
        if 'r' not in x:
            k[:, :, 2] = 0
        if 'g' not in x:
            k[:, :, 1] = 0
        if 'b' not in x:
            k[:, :, 0] = 0
        cv2.imshow(x, k)


    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
