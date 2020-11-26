import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
               help = "Image path")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
# Store height and width of the image
height, width = image.shape[:2]

quarter_height, quarter_width = height/4, width/4

# Translation Matrix T[1, 0, tx] [0 , 1, ty] .
T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]])

# using wrapAffine to transform img using matrix T
img_translation = cv2.warpAffine(image, T, (width, height))

cv2.imshow("Original Image", image)
cv2.imshow('->Translatated', img_translation)
#cv2.putText(image, 'flew', (0,10), font = cv2.FONT_HERSHEY_SIMPLEX, 
#           fontScale = 1,thickness =  2, cv2.LINE_AA, True)

k = cv2.waitKey(0)
if k == ord('s'):
    cv2.imwrite('Img_Saved.jpg', img_translation)
cv2.waitKey(0)
