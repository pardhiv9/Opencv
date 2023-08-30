#Perform Sharpening of Image using Laplacian mask implemented with an extension of diagonal neighbors

import cv2
import numpy as np
img = cv2.imread("C:/Users/ashfa/Downloads/IMG_20230825_111703.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.array([[0,1,0], [1,-4,1], [0,1,0]])
sharpened = cv2.filter2D(gray, -1, kernel)
cv2.imshow('Original', gray)
cv2.imshow('Sharpened', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
