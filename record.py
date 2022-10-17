from face_scanner import scan, list_ports
import cv2
import numpy as np

cap = cv2.VideoCapture(1)
while True:
    ret, frame = cap.read()
    output = scan(frame,cv2.CascadeClassifier('data/haarcascade/haarcascade_frontalface_default.xml'))
    cv2.imshow('frame',output)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
