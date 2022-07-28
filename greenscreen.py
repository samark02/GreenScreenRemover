import cv2
import numpy as np

video=cv2.VideoCapture("Green_Screen_Sample.mp4")
image=cv2.imread("bg1.jpg")

while True:
    ret,frame=video.read()
    frametime=15
    frame=cv2.resize(frame,(480,620))
    image=cv2.resize(image,(480,620))
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_g=np.array([32,94,112])
    u_g=np.array([145,255,255])

    mask=cv2.inRange(hsv,l_g,u_g)   
    final=cv2.bitwise_and(frame,frame,mask=mask)
    f=frame-final
    gs=np.where(f==0,image,f)

    cv2.imshow("frame",frame)
    cv2.imshow("result",gs)
    k=cv2.waitKey(frametime)
    if k==ord("x"):
        break
video.release()
cv2.destroyAllWindows()
