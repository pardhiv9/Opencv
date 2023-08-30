#Perform Edge detection using Sobel Matrix along Y axis

import cv2
img = cv2.imread("C:/Users/ashfa/Downloads/IMG_20230825_111703.jpg")
cv2.imshow('Original', img)
cv2.waitKey(0)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
desired_width = 700
desired_height = 650
img_resized = cv2.resize(sobely, (desired_width, desired_height))
cv2.imshow('Sobel Y', img_resized)
cv2.waitKey(0)
