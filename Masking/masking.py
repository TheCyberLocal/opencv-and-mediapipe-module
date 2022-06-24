import cv2

cap = cv2.VideoCapture(0)

# history=10000, varThreshold=40
object_detector = cv2.createBackgroundSubtractorMOG2()

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out_org = cv2.VideoWriter('out_org.avi', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))
out_spec = cv2.VideoWriter('out_spec.avi', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

while True:
    ret, frame = cap.read()
    height, width, _ = frame.shape
    focus = frame[340:600, 500:700]
    spec = frame
    # Object detection
    motion = False
    mask = object_detector.apply(frame)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)  # clean mask of grey pixels
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        # Calculate area and remove small elements
        area = cv2.contourArea(cnt)

        if area > 500:
            motion = True
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(spec, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.drawContours(spec, [cnt], -1, (0, 255, 0), 1)

    if motion:
        out_spec.write(spec)
    out_org.write(frame)

    cv2.imshow("frame", frame)
    cv2.imshow("focus", focus)
    cv2.imshow("mask", mask)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
out_org.release()
out_spec.release()
cv2.destroyAllWindows()
