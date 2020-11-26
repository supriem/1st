import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                help = "Path to image file")
args = vars(ap.parse_args())
print(args)

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Opencv has BGR format
(b, g, r) = image[0,0]
#print(image[0,0])
print(f"Pixel at top left is red -> {r}, green -> {g}, blue -> {b}")

# Manipulating Pixels By adding BGR(in Opencv)pixel intensity to max
image[0,0] = (0,0,255)
print(" We can see that Red pixel is Max: ",image[0,0])
(b,g,r) = image[0, 0] # sets red to 255
print("Pixel value at top left corner is red -> {}, green -> {}, blue -> {}".format(r,g,b))

# Displaying Top Left Corner
corner = image[0:100, 0:100]
cv2.imshow("Top LeftCorner", corner)


# right corner
rc = image[-100:, -100:]
cv2.imshow("Bottom Right?", rc)

# Displaying Updated
image[0:100, 0:100] = (0, 255, 0)
cv2.imshow("Updated", image)
cv2.waitKey(0)

