"""
This script compares two images using two different methods:
 -  ORB (Oriented FAST and Rotated BRIEF)
 -  Structural Similarity Index (SSIM).

Both methods are used to assess the similarity between two images.
ORB is used for feature matching, and SSIM assesses the similarity between two images.
"""

from skimage.metrics import structural_similarity  # pip install scikit-image
import cv2  # pip install opencv-python

# Function to compare images using ORB feature matching
def orb_sim(img1, img2):
    orb = cv2.ORB_create()  # Create ORB detector object

    # Detect keypoints and compute descriptors for both images
    kp_a, desc_a = orb.detectAndCompute(img1, None)
    kp_b, desc_b = orb.detectAndCompute(img2, None)

    # Create BFMatcher object with Hamming distance and cross-check
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors
    matches = bf.match(desc_a, desc_b)

    # Filter matches that are too far apart
    similar_regions = [i for i in matches if i.distance < 50]

    # Calculate similarity based on the number of good matches
    if len(matches) == 0:
        return 0
    return len(similar_regions) / len(matches)

# Function to compare images using SSIM
def structural_sim(img1, img2):
    # Calculate structural similarity
    sim, diff = structural_similarity(img1, img2, full=True)
    return sim

# Read two images in grayscale
img_1 = cv2.imread('maze1.jpg', 0)
img_2 = cv2.imread('maze2.jpg', 0)

# Calculate ORB similarity
orb_similarity = orb_sim(img_1, img_2)
print("ORB similarity:", orb_similarity)

# Calculate SSIM similarity
ssim = structural_sim(img_1, img_2)
print("SSIM similarity:", ssim)
