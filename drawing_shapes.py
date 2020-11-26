import cv2
import numpy as np


# Defining canvas of 500*500 pixels with 3 color channels
canvas = np.zeros((500, 500, 3), dtype = "uint8")

# Drawing BGR 
red = (0, 0, 255)
cv2.line(canvas, (0,0), (500, 500), red)
cv2.imshow("Canvas Red", canvas)
cv2.waitKey(0)

blue = (255, 0, 0)
cv2.line(canvas, (500, 0), (0, 500), blue)
cv2.imshow("Canvas_Blue",canvas)
cv2.waitKey(0)

random_color = (55, 100, 105)
start_point = (20,120)
end_point  = (30,180)
cv2.rectangle(canvas, start_point, end_point, random_color,1)
cv2.imshow("Canvas_With_Rect", canvas)
cv2.waitKey(0)

# Rect-2
cv2.rectangle(canvas, (400, 500), (100, 22), red, 5)
cv2.imshow("Canvas_With_Rect", canvas)
cv2.waitKey(0)

# Drawing Circles 
cv2.circle(canvas,center=(150,150),radius=100,color=(255,0,0),thickness=10)
cv2.imshow("CircleOnNewWimdow", canvas)
cv2.waitKey(0)






