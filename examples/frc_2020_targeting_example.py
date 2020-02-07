# Import Usefull Code Written by Smart People
import imutils
import numpy as np
from cv2 import cv2

def nothing(x):
    pass

cv2.namedWindow('Targeting Controls')

cv2.namedWindow('Test Image')

# load images
images = []
images.append(cv2.imread("./resources/img/frc1.jpg"))
images.append(cv2.imread("./resources/img/frc2.jpg"))
images.append(cv2.imread("./resources/img/frc3.jpg"))
images.append(cv2.imread("./resources/img/frc4.jpg"))
images.append(cv2.imread("./resources/img/frc5.jpg"))
images.append(cv2.imread("./resources/img/frc6.jpg"))
images.append(cv2.imread("./resources/img/frc7.jpg"))
images.append(cv2.imread("./resources/img/frc8.jpg"))
images.append(cv2.imread("./resources/img/frc9.jpg"))
images.append(cv2.imread("./resources/img/test0.jpg"))


cv2.createTrackbar('Image','Targeting Controls',0,len(images)-1,nothing)

# create trackbars for HSV
cv2.createTrackbar('H Upper','Targeting Controls',0,255,nothing)
cv2.createTrackbar('S Upper','Targeting Controls',0,255,nothing)
cv2.createTrackbar('V Upper','Targeting Controls',0,255,nothing)
cv2.createTrackbar('H Lower','Targeting Controls',0,255,nothing)
cv2.createTrackbar('S Lower','Targeting Controls',0,255,nothing)
cv2.createTrackbar('V Lower','Targeting Controls',0,255,nothing)

cv2.createTrackbar('M Area','Targeting Controls',0,10000,nothing)



while(1):
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    
    img = images[cv2.getTrackbarPos('Image','Targeting Controls')].copy()

    # Define range of target colors in HSV
    lowerColor = np.array([cv2.getTrackbarPos('H Lower','Targeting Controls'),cv2.getTrackbarPos('S Lower','Targeting Controls'),cv2.getTrackbarPos('V Lower','Targeting Controls')])
    upperColor = np.array([cv2.getTrackbarPos('H Upper','Targeting Controls'),cv2.getTrackbarPos('S Upper','Targeting Controls'),cv2.getTrackbarPos('V Upper','Targeting Controls')])

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)            # Convert image to HSV colorspace for processing
    gray = cv2.inRange(hsv, lowerColor, upperColor)         # Generate mask from color range

    # Find countours in image with OpenCV
    cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    # Draw/print contour information
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)                            # get the bounding box
        area = w*h                                                  # calculate bounding box area
        center = (int(x + w/2), int(y + h/2))                       # calculate center

        # skip contours with too small area
        if (w*h) < cv2.getTrackbarPos('M Area','Targeting Controls'):
            continue

        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)    # draw green bounding box

        cv2.circle(img, center, 2, (255, 0, 0), 2)                # draw blue centerpoint

    
        rect = cv2.minAreaRect(c)                                   # get the min area rectangle
        box = cv2.boxPoints(rect)                                   # extract box points for drawing
        cv2.drawContours(img, [np.int0(box)], 0, (0, 0, 255))     # draw red min area rectangle

    cv2.imshow('Test Image',img)

cv2.destroyAllWindows()