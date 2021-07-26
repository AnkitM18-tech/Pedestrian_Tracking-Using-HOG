import cv2
import imutils
from human_detection import Detector

image = cv2.imread('people.jpg')
image = imutils.resize(image,width=900)
image = Detector(image)
cv2.waitKey(0)
cv2.destroyAllWindows()