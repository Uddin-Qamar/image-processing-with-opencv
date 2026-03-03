# To draw figure : ractangle, circle, line and text on image
import cv2
import matplotlib.pyplot as plt
import numpy as np

imgPath = cv2.imread("images/inputImg.jpg")

img = cv2.cvtColor(imgPath, cv2.COLOR_BGR2RGB)

if imgPath is None:
    raise FileNotFoundError("The image in the given path dosn't exist")

#Make a copy of the image
cpyImg = img.copy()

# resize the image: make it smaller to fir in the screen
bgrImg = cv2.resize(cpyImg, (1200, 800))
newImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)
#to print the size of the image in the terminal to make sure it get resized
height, width = newImg.shape[:2]
print("image size", (height, width))

# draw a line on the new image
cv2.line(newImg, (50, 50), (580,50), (0, 0, 250), thickness =5)

# draw a rectangle
cv2.rectangle(newImg, (900, 20), (1050, 150), (200,100,0), thickness = 4)

# draw some text on the image

cv2.putText(newImg,"Harvestor Machine", (400,100), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,20), thickness =2)

# draw a circle there in the image
cv2.circle(newImg, (300,500), 80, (0, 255, 0), thickness = -1)

# To draw a triangle in the image.

pts = np.array([[400,130],[600,130], [380,400]], dtype = np.int32)
cv2.polylines(newImg, [pts], isClosed = True, color =(2, 2, 253), thickness =2)

# Finally saving the edited image
outputImg_path = "images/result.jpg"
cv2.imwrite(outputImg_path, newImg)
print("The edited image is saved in the output image directory")

# show the image in the windows
cv2.imshow("Drawings", newImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
