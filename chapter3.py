#RESIZE IMAGE AND CROPPING
import cv2

img = cv2.imread('Resources/lena.png')
print(img.shape)

imgResize= cv2.resize(img,(100,100))
print(imgResize.shape)

imgCropped = img[0:200,200:225]

cv2.imshow('Ori Image',img)
cv2.imshow('Resize image',imgResize)
cv2.imshow('Image Cropped',imgCropped)
cv2.waitKey(0)