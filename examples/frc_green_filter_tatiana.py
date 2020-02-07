# necessary imports (no forgetting these!)
import imutils
import numpy as np    #recall that numpy and opencv have funky imports
from cv2 import cv2


image = cv2.imread("./resources/img/frc1.jpg")        # grab the test image
# print(image)  #print the image for testing file paths purposes 


'''Variable info'''
(height, width, depth) = image.shape   # use opencv to get the image dimensions 
imgSize = image.size                   # use opencv to grab image size (num of pixels)
imgDataType = image.dtype              # once again use opencv to get the image data type 
contourImg = image                     # keep a copy of the original image


# print new variables to console to check they got swiped correctly 
print("width={}, height={}, depth={}".format(width, height, depth))
print("size={}, data type={}".format(imgSize, imgDataType))                              # -->unimportant side note, but I want to figure out how to skip lines/add space. 


# define range of HSV values (for filtering FRC green LED on reflected tape)
lowerColor = np.array([63,150,95])
upperColor = np.array([79,255,255])

# finally do the processing part 
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)            # convert image to HSV for processing
mask = cv2.inRange(hsv, lowerColor, upperColor)         # generate mask from set HSV ranges
image = cv2.bitwise_and(image,image, mask= mask)        # make mask of origional image\

# find countours in image with OpenCV
contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)


# draw and print contour information
print("\nContour Information:")
for n in contours:
    x, y, w, h = cv2.boundingRect(n)       # get the bounding box
    area = w*h                             # calculate bounding box area
    center = (int(x + w/2), int(y + h/2))  # calculate center

    cv2.rectangle(contourImg, (x, y), (x+w, y+h), (0, 255, 0), 1)    # draw green bounding box
    cv2.circle(contourImg, center, 2, (255, 50, 0), 2)               # draw blue centerpoint
    
    rect = cv2.minAreaRect(n)                                        # get the min area rectangle
    box = cv2.boxPoints(rect)                                        # extract box points for drawing
    cv2.drawContours(contourImg, [np.int0(box)], 0, (0, 0, 255))     # draw red min area rectangle

    print("\n\t-bounding box-\n\tx={}\ty={}\n\tw={}\th={}\n\tcenter={}\n\tarea={}".format(x, y, w, h, center, area))




cv2.imshow("Mask", mask)              # displays image mask 
cv2.imshow("Filtered", image)         # displays filtered original image
cv2.imshow("Contours", contourImg)    # displays image mask

cv2.waitKey(0)                     # wait for a keypress to close
