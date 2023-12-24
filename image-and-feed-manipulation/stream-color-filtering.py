"""
This script demonstrates how to filter a specific color
 (in this case, blue) from a live video feed using OpenCV and NumPy.
The color choice can be easily changed by adjusting the HSV color range values.
To filter a different color, simply change the lower_blue and upper_blue arrays to the desired color's HSV range.
The script works by converting the frame to HSV (Hue, Saturation, Value) color space,
 which is more suitable for color filtering compared to the RGB color space.
"""

import numpy as np  # pip install numpy
import cv2  # pip install opencv-python

# Start capturing video from the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Read each frame
    width = int(cap.get(3))  # Get the frame's width
    height = int(cap.get(4))  # Get the frame's height

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds of the color to filter (blue in this case)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Create a mask that captures only the parts of the frame within the color range
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Apply the mask to the original frame
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the original frame and the masked frame
    cv2.imshow('frame', result)
    cv2.imshow('mask', mask)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
