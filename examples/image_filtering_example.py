# Import Usefull Code Written by Smart People
import imutils
import numpy as np
from cv2 import cv2

image = cv2.imread("./resources/img/test0.jpg")        # Load image

(h, w, d) = image.shape             # Extract image dimensions to variables h, w, & d
size = image.size                   # Extrace image size (num. pixles) to variable size
dtype = image.dtype                 # Extract image data type to variable dtype


#Print Useful Information to Console
print("width={}, height={}, depth={}".format(w, h, d))
print("size={}, data type={}".format(size, dtype))

oImage = image                                          # Save a copy of the origional image in memory

# Define range of target colors in HSV
lowerColor = np.array([44,63,63])
upperColor = np.array([52,255,255])

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)            # Convert image to HSV colorspace for processing
mask = cv2.inRange(hsv, lowerColor, upperColor)         # Generate mask from color range
image = cv2.bitwise_and(image,image, mask= mask)        # Mask origional image

cv2.imshow("Origional", oImage)                          # Display origional image
cv2.imshow("Mask", mask)                                # Display image mask
cv2.imshow("Filtered", image)                           # Display filtered image
cv2.waitKey(0)                                          # Wait for keypress to close

