import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "blobs_in_circular_arrangement.tif"

img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
if img is not None:
    print("Shape:", img.shape, "dtype", img.dtype)

# Complement:  inverse of the image

inv = cv2.bitwise_not(img)

# Convet grascale image into binary image

ret, binary = cv2.threshold(inv, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Define the kernal/structuring matrix size
k_open = 11
k_close = 25
# define structuring element for both open and close
s_open = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (k_open,k_close))
s_close = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (k_open,k_close))

# opening: find the smaller blobs in the image 
smaller_region = cv2.morphologyEx(binary, cv2.MORPH_OPEN, s_open)

# Colosing: larger blobs region
large_region = cv2.morphologyEx(smaller_region, cv2.MORPH_CLOSE, s_close)
# Boundary of the blobs 
boundry = cv2.morphologyEx(large_region, cv2.MORPH_GRADIENT, np.ones((3,3), np.uint8))

# Display them 
plt.figure(figsize=(8,8))
plt.subplot(2,2,1)
plt.imshow(img)
plt.title("Original image")
plt.axis("off")
plt.subplot(2,2,2)
plt.imshow(boundry, cmap="gray")
plt.title("Bounday of the blobs")

plt.subplot(2,2,3)
plt.imshow(smaller_region, cmap="gray")
plt.title("Open")

plt.subplot(2,2,4)
plt.imshow(large_region, cmap="gray")
plt.title("Closed")

plt.show()
