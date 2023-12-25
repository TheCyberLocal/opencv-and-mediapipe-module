"""
This script reads each image from the specified input directory,
 processes it to create a sketch, and then saves the sketch to the specified output directory.
Remember to replace 'images/' and 'sketches/' with your actual directory paths.
"""

import cv2  # pip install opencv-python
import glob  # pip install glob
import os  # pip install os

# Directory containing the images
input_dir = 'images/'
# Directory where sketches will be saved
output_dir = 'sketches/'

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get all JPG image paths from the input directory
image_paths = glob.glob(input_dir + '*.jpg')

for image_path in image_paths:
    # Read the image
    image = cv2.imread(image_path)
    # Convert to grayscale
    grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Invert the grayscale image
    inverted_grey = 255 - grey_img
    # Apply Gaussian blur
    blur = cv2.GaussianBlur(inverted_grey, (21, 21), 0)
    # Invert the blurred image
    inverted_blur = cv2.bitwise_not(blur)
    # Create the pencil sketch effect
    sketch = cv2.divide(grey_img, inverted_blur, scale=256.0)

    # Extract the filename from the path and create the output path
    filename = os.path.basename(image_path)
    output_path = os.path.join(output_dir, str(filename)[:-4] + '_sketch.jpg')

    # Save the sketch
    cv2.imwrite(output_path, sketch)

# Close all windows
cv2.destroyAllWindows()
