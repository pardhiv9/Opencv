#Perform basic video processing operations on the captured video• Read captured video in python and display the video, in slow motion and in fast motion.

import cv2
import numpy as np
cap = cv2.VideoCapture("C:/Users/ashfa/Videos/Captures/video_20230825_133025_edit.mp4")
if (cap.isOpened()== False):
    print("Error opening video file")
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(250) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
