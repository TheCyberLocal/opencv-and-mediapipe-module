import cv2
import datetime

cap = cv2.VideoCapture(1)
positive = 0

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out_org = cv2.VideoWriter('out_org.avi', fourcc, 10.0, (int(cap.get(3)), int(cap.get(4))))
object_detector = cv2.createBackgroundSubtractorMOG2()
font = cv2.FONT_HERSHEY_PLAIN
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    mask = object_detector.apply(frame)

    positive = 0

    for x in range(height):
        for y in range(width):
            positive += mask[x][y]

    text = str(datetime.datetime.now())[:-7]
    frame = cv2.putText(frame, text, (10, height - 20), font, 1, (0, 0, 255), 1, cv2.LINE_AA)
    print(positive)
    if positive > 3000000:
        print('motion detected')
        out_org.write(frame)
    else:
        print('no motion detected')

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    last = mask.copy()

    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
out_org.release()
cv2.destroyAllWindows()
