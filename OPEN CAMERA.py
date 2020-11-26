import cv2


cap=cv2.VideoCapture(-1);#default camera will be at index 0or -1   ,2nd cam will be at index 1,2,etc


while(True):
    ret,frame=cap.read()  #frame var

    gray=cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2GRAY)  #WILL CAPTURE GRAYSCALE IMAGE

    cv2.imshow('frame',gray)  #show frame inside indow

    if cv2.waitKey(1) &0xFF==ord('q'):            #on pressing q windows will closED
                                                  #that was mask for 64 bit sys
        break                                     #this function will read video

cap.release()                                     #we have to release
cv2.destroyAllWindows()

