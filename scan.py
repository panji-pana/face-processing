import numpy as np
import cv2
from face_scanner import scan

#Loading the image to be tested
image = "ludwig.jpg"
directory = f'C:/Users/isabe/Documents/dev/else/face processing/data/inputs/{image}'
input_image = cv2.imread(directory)
cscd = cv2.CascadeClassifier('data/haarcascade/haarcascade_frontalface_default.xml')

output = scan(input_image,cscd)
cv2.imshow('Output',output)
cv2.imwrite(f'C:/Users/isabe/Documents/dev/else/face processing/data/outputs/{image}',output)
cv2.waitKey(0)
cv2.destroyAllWindows()