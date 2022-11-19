import cv2

#read image
img=cv2.imread('butterfly.jpg')

#display colour image
cv2.imshow('Display Image',img)

#convert colour image to grayscale
gray_img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

#display grayscale image
cv2.imshow('Grayscale',gray_img)

cv2.waitKey(0)