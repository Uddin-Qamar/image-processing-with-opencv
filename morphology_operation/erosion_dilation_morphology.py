
import cv2
import numpy as np
import matplotlib.pyplot as plt


#----------------------------#Task 1----------------------------
# read image grayscale image with broken text
img = cv2.imread("broken-text.tif", 0)

# convert to binary
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# structuring element (size depends on break length)
kernel = np.ones((3,3), np.uint8)

# dilation
dilated = cv2.dilate(binary, kernel, iterations=1)


#----------------------------#Task 2----------------------------
# Read Binary image and perform erosion to remove the small wires

binary_img_path = "wirebond-mask.tif"

img = cv2.imread(binary_img_path, cv2.IMREAD_GRAYSCALE)
print("img is None?", img is None)
if img is not None:
    print("shape:", img.shape, "dtype:", img.dtype)
    print("unique values (first 20):", np.unique(img))

# Choose structuring element
# Must fit inside center square + thick pads, but NOT fit inside thin wires.
k = 14 # Value of k can be 5, 7 or more 
se = cv2.getStructuringElement(cv2.MORPH_RECT, (k, k)) # Other Kernel methids : CROSS , ELLIPSE

# 4) Erode to remove thin wires, then dilate to restore thick structures = this is called opening
eroded = cv2.erode(img, se, iterations=1)
restored = cv2.dilate(eroded, se, iterations=1)


# display the binray and dialated image of Task-1

plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
plt.imshow(binary, cmap='gray')
plt.title("Original")

plt.subplot(2,2,2)
plt.imshow(dilated, cmap='gray')
plt.title("Dilated")


# display original binary image with small wire and erroded image without wire of Task-2
plt.subplot(2,2,3)
plt.imshow(img, cmap="gray")
plt.title("Original Binary Image with Wire")


plt.subplot(2,2,4)
plt.imshow(restored, cmap="gray")
plt.title(" Opening = Eroded + Dilate (wires removed)")

plt.show()


# 6) Optional: save Task-2 eroded image without wire result
out_path = "wirebond-mask_no-wires.png"
cv2.imwrite(out_path, restored)
print("Saved:", out_path)

