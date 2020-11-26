import cv2
#create a cascade classifier object
face_cascade=cv2.CascadeClassifier("messi.jpg")

#reading the image as it is

img=cv2.imread("messi.jpg")



#reading the image as gray scale image


gray_img=cv2.cvtColor(img,cv2.COLOR_BAYER_BG2GRAY)


#search the corodinate of image

faces=face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)

print((type(faces)))
print(faces)

for x,y,w,h in faces:
    img=cv2.rectanglr(img,(x,y),(x+w,y+h),(0,255,0),3)

resized=cv2.resize(img,(int(img.shape[1]),int(img.shape[0])))

cv2.imshow("Gray",resized)

cv2.waitKey(0)
cv2.destroyAllWindows()