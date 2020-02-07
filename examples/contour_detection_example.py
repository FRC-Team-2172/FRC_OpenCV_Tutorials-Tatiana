# Import Usefull Code Written by Smart People
import imutils
import numpy as np
from cv2 import cv2

image = cv2.imread("./resources/img/test0.jpg")        # Load image

(h, w, d) = image.shape             # Extract image dimensions to variables h, w, & d
size = image.size                   # Extrace image size (num. pixles) to variable size
dtype = image.dtype                 # Extract image data type to variable dtype


#Print Useful Information to Console
print("\nFile Information:")
print("width={}\theight={}\tdepth={}".format(w, h, d))
print("size={}\tdata type={}\n".format(size, dtype))


# Define range of target colors in HSV
lowerColor = np.array([44,63,63])
upperColor = np.array([52,255,255])

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)            # Convert image to HSV colorspace for processing
gray = cv2.inRange(hsv, lowerColor, upperColor)         # Generate mask from color range

# Find countours in image with OpenCV
cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# Draw/print contour information
print("\nContour Information:")
for c in cnts:
    x, y, w, h = cv2.boundingRect(c)                            # get the bounding box
    area = w*h                                                  # calculate bounding box area
    center = (int(x + w/2), int(y + h/2))                       # calculate center

    # skip contours with too small area
    if (w*h) < 1000:
        continue

    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 1)    # draw green bounding box

    cv2.circle(image, center, 2, (255, 0, 0), 2)                # draw blue centerpoint
    
    rect = cv2.minAreaRect(c)                                   # get the min area rectangle
    box = cv2.boxPoints(rect)                                   # extract box points for drawing
    cv2.drawContours(image, [np.int0(box)], 0, (0, 0, 255))     # draw red min area rectangle

    print("\n\t-bounding box-\n\tx={}\ty={}\n\tw={}\th={}\n\tcenter={}\n\tarea={}".format(x, y, w, h, center, area))



    


cv2.imshow("Mask", gray)                              # Display image mask
cv2.imshow("Shapes", image)                           # Display image with shapes

cv2.waitKey(0)