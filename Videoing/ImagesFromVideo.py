# organize imports
import cv2

# This will return video from the first webcam on your computer.
cap = cv2.VideoCapture(0)

location = "D:\\PyCharm_Database\\ObjectDetection\\TFODCourse\\Tensorflow\\workspace\\images\\videofeed\\"

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_out.avi', fourcc, 20.0, (640, 480))
# loop runs if capturing has been initialized.
photo = 0
while True:
    photo += 1
    # reads frames from a camera
    # ret checks return at each frame
    ret, frame = cap.read()

    # Converts to HSV color space, OCV reads colors as BGR
    # frame is converted to hsv

    # output the frame
    cv2.imwrite(f'{location}{photo}.jpg', frame)

    # The original input frame is shown in the window
    cv2.imshow('Original', frame)

    # Wait for 'a' key to stop the program
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

# Close the window / Release webcam
cap.release()

# After we release our webcam, we also release the output
out.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()
