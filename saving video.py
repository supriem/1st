import cv2
cap=cv2.VideoCapture(0);  #this is a class for capturing the video#this is video capture calss
out=cv2.VideoWriter
print(cap.isOpened())
while(cap.isOpened()):
    ret,frame=cap.read()
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))   #we can use differents functions such as this.#watch video flags documentation for detail
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    gray=cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2GRAY)
    cv2.imshow('frame',gray)


    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
capp.release()
cv2.destroyAllWindows()

# #
# 640.0  width and height by default
# 480.0