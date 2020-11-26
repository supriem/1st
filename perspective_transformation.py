import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Locate points of the documents or object which 
    points_1 = np.float32([[0, 260], [640, 260], [0, 400], []])


