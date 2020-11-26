import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
               help = "Insert path to image in terminal")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original_Img", image)

M = np.float32([[1, 0, 40], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, 
                         (image.shape[1], image.shape[0]))
cv2.imshow("Shifting Down(+ty) and Right(+tx)", shifted)
M = np.float32([[1, 0, -80], [0, 1, -100]])
next_shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", next_shifted)
cv2.waitKey(0)
