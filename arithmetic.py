import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
               help = "Image path")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

print("max of 255: {}".format(cv2.add(np.uint8([200]), np.uint8([100])))) # adding color channel to make 300 but can we?

print("min of 0: {}".format(cv2.subtract(np.uint8([50]), np.uint8
([100]))))

print("wrap around: {}".format(np.uint8([200]) + 
                               np.uint8([100])))
print("wrap around: {}".format(np.uint8([50]) - np.uint8([100])))

# Performing Arithmetic Operations on Image
M = np.ones(image.shape, dtype = "uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Added(Should Be Brighter)", added)

M = np.ones(image.shape, dtype = "uint8") * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)
cv2.waitKey(0)

