"""
This script demonstrates how to use OpenCV to capture video from a webcam,
 with a trackbar to adjust the camera's focus.
The utility is when creating your own image recognition library,
 or training your own DNN to recognize an image based on your training image set.
"""

import cv2  # pip install opencv-python
import os  # pip install os

# Function to be called when trackbar value changes. Currently does nothing.
def empty(a):
    pass

# Ensure 'Library' folder exists
if not os.path.exists('Library'):
    os.makedirs('Library')

# Capture video from the first webcam on the computer.
cap = cv2.VideoCapture(0)
frameWidth, frameHeight = 640, 480
cap.set(3, frameWidth)  # Set the width of the video frame.
cap.set(4, frameHeight)  # Set the height of the video frame.

# Create a window for the trackbar.
cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 640, 60)
cv2.createTrackbar("Focus", "Parameters", 0, 255, empty)  # Create a trackbar for adjusting focus.

print(cv2.getTrackbarPos("Focus", "Parameters"))  # Print the current focus value.
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Print frame dimensions.

id_type, id_num = 'Cards', 1  # Variables for saving images.

while True:
    ret, frame = cap.read()  # Read a frame from the video capture.
    cap.set(28, cv2.getTrackbarPos("Focus", "Parameters"))  # Set the camera focus based on trackbar position.

    cv2.imshow('original', frame)  # Display the captured frame.

    # Save the frame as an image file when 's' is pressed.
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite(f'Library\\{id_type}-{id_num}.png', frame)
        print(f'took photo: {id_num}')
        id_num += 1

    # Break the loop when 'q' is pressed.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all OpenCV windows.
cap.release()
cv2.destroyAllWindows()
