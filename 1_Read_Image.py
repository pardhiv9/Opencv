#To Perform basic Image Handling and processing operations on the image. Read an image in python and Convert an Image to Grayscale

import cv2
image_path = "C:/Users/ashfa/Downloads/IMG_20230825_111703.jpg"
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
desired_width = 700
desired_height = 650
img_resized1 = cv2.resize(gray_image, (desired_width, desired_height))
img_resized2 = cv2.resize(image, (desired_width, desired_height))
cv2.imshow('Original Image', img_resized2)
cv2.imshow('Grayscale Image', img_resized1)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
