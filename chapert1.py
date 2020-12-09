import cv2
import numpy as np

#import image
# img = cv2.imread("Resource/lena.jfif")
# cv2.imshow("Output",img)
# cv2.waitKey(0)

#import video
# cap = cv2.VideoCapture("Resource/11618.t.mp4")
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(2) & 0xFF == ord('q'):
#         break

# #import webcam
cap = cv2.VideoCapture(0)
# ini width
cap.set(3,640)
# ini setting height
cap.set(4,480)
#ini setting brightness
cap.set(10,100)

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

# ini buat ngerubah gambar jadi gray
# img = cv2.imread("Resource/lena.jfif")
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray Image",imgGray)
# cv2.waitKey(0)

