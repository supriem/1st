import numpy as  np
import cv2

rectangle  = np.zeros((300, 300), dtype = "uint8")
cv2.rectangle(rectangle, start_point = (25, 25), end_point = (275, 275), (255, -1))
cv2.imshow("Rectangle", rectangle)

circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, thickness = -1)
cv2.imshow("Circle", circle)


