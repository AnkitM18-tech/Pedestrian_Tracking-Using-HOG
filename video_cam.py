import cv2
from human_detection import Detector

cap = cv2.VideoCapture('walk.mp4')


while True:
    ret, frame = cap.read()
    frame = Detector(frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()