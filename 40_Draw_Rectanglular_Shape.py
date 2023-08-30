#Draw Rectangular shape and extract objects

import cv2
img = cv2.imread("C:/Users/ashfa/Downloads/IMG_20230825_111703.jpg")
x, y = 700, 600
width, height = 700, 650
roi = img[y:y+height, x:x+width]
cv2.imshow('ROI', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
