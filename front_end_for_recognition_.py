

from PIL import Image

import cv2
from keras.models import load_model
import numpy as np

import numpy as np
from keras.preprocessing import image

from keras.preprocessing import image
model = load_model('VGG16_fingercount_8jan_50epochs.h5')

roi_top = 20
roi_bottom = 300
roi_right = 300
roi_left = 600

cam = cv2.VideoCapture(0)
while True:
    
    ret,frame = cam.read()
    frame = cv2.flip(frame,1)
    if ret == True:
    
  

        frame_copy = frame.copy()
        cv2.rectangle(frame_copy, (roi_left, roi_top), (roi_right, roi_bottom), (0,0,255), 5)
        roi = frame[roi_top:roi_bottom, roi_right:roi_left]
        
        
        finger = cv2.resize(roi,(224,224))
        im =  Image.fromarray(finger, 'RGB')
        im_array = np.array(im)
        im_array_exp_dim = np.expand_dims(im_array, axis=0)
        predict = model.predict(im_array_exp_dim)
        print(predict)
        
        if(predict[0][0]>0.5):
            name = "1"
            cv2.putText(frame_copy,name, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            
        elif(predict[0][1]>0.5):
            name = "2"
            cv2.putText(frame_copy,name, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            
        elif(predict[0][2]>0.5):
            name = "3"
            cv2.putText(frame_copy,name, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            
        elif(predict[0][3]>0.5):
            name = "4"
            cv2.putText(frame_copy,name, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            
        elif(predict[0][4]>0.5):
            name = "5"
            cv2.putText(frame_copy,name, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            
        else:
            cv2.putText(frame_copy,"Not found",(50,50), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            
            
            
            
        
            
            
            

    cv2.imshow("Video", frame_copy)
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break
            
cam.release()
cv2.destroyAllWindows()





