# necessary imports (no forgetting these!)
import imutils
import numpy as np    #recall that numpy and opencv have funky imports
from cv2 import cv2

# create VideoCapture object
camera = cv2.VideoCapture(0)  # passing a value of zero gets either the only USB camera feed or the default


while(True):
    # Capture frame-by-frame
    ret, frame = camera.read()

    # Our operations on the frame come here
    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', hsv)
    if cv2.waitKey(1) & 0xFF == 27:
        break

# When everything done, release the capture
camera.release()
cv2.destroyAllWindows()