#Contours / Shape Detection
import cv2

def getContours(img):
    countours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in countours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:
            #contour
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            # print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            if objCor == 3:
                shape = "Triangle"
            elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio >= 1 and aspRatio <= 1.05:
                    shape = "Square"
                else:
                    shape = "Rectangle"
            else:
                shape = "Circle"
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContour,shape,
                        (x+(w//2)-10,y+(h//2)-10),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.5,
                        (0,0,0),
                        2)
img = cv2.imread("Resources/shapes.png")
imgContour = img.copy()

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
getContours(imgCanny)


cv2.imshow("Original",img)
#merubah menjadi grayscale
# cv2.imshow("Gray",imgGray)
#membuat blur
# cv2.imshow("Blur",imgBlur)
# cv2.imshow("Canny",imgCanny)
cv2.imshow("Contour",imgContour)
cv2.waitKey(0)