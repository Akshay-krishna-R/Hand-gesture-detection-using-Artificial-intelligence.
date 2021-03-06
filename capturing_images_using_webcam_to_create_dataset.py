

import cv2
import numpy as np

import numpy as np
from keras.preprocessing import image

roi_top = 20
roi_bottom = 300
roi_right = 300
roi_left = 600

cam = cv2.VideoCapture(0)
count = 0
while True:
    ret,frame = cam.read()
    frame = cv2.flip(frame, 1)
    if ret == True:
        count +=1
        frame_copy = frame.copy()
        
        cv2.rectangle(frame_copy, (roi_left, roi_top), (roi_right, roi_bottom), (0,0,255), 5)
        roi = frame[roi_top:roi_bottom, roi_right:roi_left]

     
        file_name_path = './Images/' + str(count) + '.jpg'
        cv2.imwrite(file_name_path,roi)
        cv2.putText(frame_copy, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
        cv2.imshow('capturing window', frame_copy )
        
        
    if cv2.waitKey(25) & 0xFF == ord('q') :
        break
        

        
cam.release()
cv2.destroyAllWindows()



