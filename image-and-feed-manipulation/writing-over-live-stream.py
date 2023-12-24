"""
The script continuously reads frames from the webcam,
 applies different drawing functions on each frame,
 and displays the modified frame in real-time.
It stops and exits when the user presses the 'q' key.
This example is a good starting point to understand
 how to overlay graphics on video streams using OpenCV.
"""

import cv2  # Import OpenCV library

# Start capturing video from webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Capture each frame
    width = int(cap.get(3))  # Get the width of the frame
    height = int(cap.get(4))  # Get the height of the frame

    # Draw lines on the frame
    img = cv2.line(frame, (0, 0), (width, height), (0, 255, 0), 10)  # Green line from top-left to bottom-right
    img = cv2.line(img, (0, int(height/2)), (width, int(height/2)), (0, 0, 255), 10)  # Red line in the middle

    # Draw a rectangle
    img = cv2.rectangle(img, (100, 100), (300, 200), (255, 0, 0), 10)  # Blue rectangle

    # Draw a filled circle
    img = cv2.circle(img, (200, 400), 60, (0, 0, 255), -1)  # Red filled circle

    # Put text on the frame
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = "I learned how to write over videofeed"
    img = cv2.putText(img, text, (10, 50), font, 1, (0, 100, 100), 2, cv2.LINE_AA)

    # Display the frame with drawings
    cv2.imshow('frame', img)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
