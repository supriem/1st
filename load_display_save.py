# OpenCV-Python Program to Read image from files
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
               help = "Path to the image")
args = vars(ap.parse_args())

image  = cv2.imread(args["image"])
#print(image.shape[0],"*", image.shape[1], "*", image.shape[2])
print(image.shape)
cv2.imshow("Image", image)
cv2.waitKey(0)

# Saving image
cv2.imwrite("saved_img", image)
