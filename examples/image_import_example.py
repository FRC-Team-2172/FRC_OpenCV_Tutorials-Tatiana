# Import Usefull Code Written by Smart People
import imutils
from cv2 import cv2    # Strange import because python :/

image = cv2.imread("./resources/img/test0.jpg")        # Load image

(h, w, d) = image.shape             # Extract image dimensions to variables h, w, & d
size = image.size                   # Extrace image size (num. pixles) to variable size
dtype = image.dtype                 # Extract image data type to variable dtype


#Print Useful Information to Console
print("width={}, height={}, depth={}".format(w, h, d))
print("size={}, data type={}".format(size, dtype))


cv2.imshow("Image", image)          # Display image
cv2.waitKey(0)                      # Wait for keypress to close