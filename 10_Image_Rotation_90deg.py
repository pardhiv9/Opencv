#The Aim of the Experiment is to perform Rotation of an image along 90 degree.

import cv2
path = "C:/Users/ashfa/Downloads/IMG_20230825_111703.jpg"
src = cv2.imread(path)
window_name = 'Image'
image = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)
img = cv2.resize(image,(700,650))
cv2.imshow(window_name, img)
cv2.waitKey(0)
