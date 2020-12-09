#Face Detection
import cv2
width = 640
height = 480
cap = cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)
cap.set(10,150)


while True:
    success, img = cap.read()
    faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow("Video",img)
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
