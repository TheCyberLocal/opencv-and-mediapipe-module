"""
This script creates an interesting effect by dividing the video frame into four quadrants
 and placing differently rotated versions of a smaller frame into each quadrant.
The video feed is displayed in a window, and the script exits if the 'q' key is pressed.
"""

import numpy as np  # pip install numpy
import cv2  # pip install opencv-python

cap = cv2.VideoCapture(0)  # Start capturing video from the first camera device

while True:
    ret, frame = cap.read()  # Read a frame from the video capture
    width = int(cap.get(3))  # Get the width of the frame
    height = int(cap.get(4))  # Get the height of the frame

    image = np.zeros(frame.shape, np.uint8)  # Create a black image of the same size as the frame
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)  # Resize the frame to half its size

    # Place different transformations of the smaller frame into the black image
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)  # Top left quadrant
    image[height//2:, :width//2] = smaller_frame  # Bottom left quadrant
    image[:height//2, width//2:] = smaller_frame  # Top right quadrant
    image[height//2:, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)  # Bottom right quadrant

    cv2.imshow('frame', image)  # Display the final image

    if cv2.waitKey(1) == ord('q'):  # Exit loop if 'q' key is pressed
        break

cap.release()  # Release the video capture object
cv2.destroyAllWindows()  # Close all OpenCV windows
