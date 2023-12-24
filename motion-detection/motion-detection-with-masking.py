"""
This script will display two windows, one showing the original video feed
 and the other showing the mask used for detecting motion.
Detected moving objects are highlighted with blue rectangles and green contours.
The script saves two videos: the original stream and the one with detections.
The script ends when the 'q' key is pressed.
"""

import cv2  # Import OpenCV library

# Initialize video capture from the webcam
cap = cv2.VideoCapture(0)

# Create a background subtractor object for motion detection
object_detector = cv2.createBackgroundSubtractorMOG2()

# Video writers to save the original and processed videos
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out_org = cv2.VideoWriter('out_org.avi', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))
out_spec = cv2.VideoWriter('out_spec.avi', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

while True:
    ret, frame = cap.read()  # Read a frame from the webcam
    height, width, _ = frame.shape  # Get frame dimensions
    # focus = frame[340:600, 500:700]  # Uncomment to create focus frame

    # Object detection setup
    motion = False
    mask = object_detector.apply(frame)  # Apply background subtraction
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)  # Clean mask of grey pixels
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate over contours to find significant motions
    for cnt in contours:
        area = cv2.contourArea(cnt)  # Calculate area of the contour
        if area > 500:  # Filter out small contours
            motion = True
            x, y, w, h = cv2.boundingRect(cnt)  # Get bounding box for the contour
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Draw rectangle around moving object
            cv2.drawContours(frame, [cnt], -1, (0, 255, 0), 1)  # Draw contour

    # Write frames to output if motion is detected
    if motion:
        out_spec.write(frame)
    out_org.write(frame)

    # Display frames in windows
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    # cv2.imshow("focus", focus)  # Uncomment if you want to see the focus

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release resources
cap.release()
out_org.release()
out_spec.release()
cv2.destroyAllWindows()
