import cv2
import numpy as np

width = 640
height = 480
cap = cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)
cap.set(10,150)

myColors = [[54,63,79,179,255,253],#hijau
            [116,22,129,167,93,215],#pink
            [4,62,83,13,190,231]] #oren
myColorValue = [
                [85,255,0],
                [242,0,255],
                [0,174,255]
                ]
myPoints = [] #[x,y,colorId]
def getContours(img):
    countours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in countours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:
            #untuk menggambar contour
            # cv2.drawContours(imgResult,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            # print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y

def findColor(img,myColors,myColorValues):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count = 0
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x,y=getContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED)
        count +=1
        # cv2.imshow(str(color[0]),mask)
def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(imgResult,(point[0],point[1], 10, myColorValues[point[2]], cv2.FILLED))
while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img,myColors, myColorValues)
    findColor(img, myColors,myColorValue)
    cv2.imshow("Result",imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

