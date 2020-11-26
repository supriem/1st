import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
        help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args[ "image"])
cv2.imshow("Original", image)

mask = np.zeros(image.shape[:2], dtype = "uint8")
#(cX, cY) = (image.shape[1] //2, image.shape[0] //2)

# Adjusting Mask to Clip slobro's face
cX, cY = 82, 28
cv2.rectangle(mask, (cX, cY), (cX + 195, cY + 150), 255, -1)  
#cv2.rectangle(mask, (cX -75, cY - 75), (cX + 75, cY + 75), 255, -1)

cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)

# Another
# initializing mask again
mask = np.zeros(image.shape[:2], dtype = "uint8")
cv2.circle(mask, (150, 100), 100, 255, -1)
masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Mask", mask)
cv2.imshow("Mask Applied to Image",  masked)
cv2.waitKey(0)


