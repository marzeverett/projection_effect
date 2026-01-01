import datetime
import os
import time
import random
import cv2 as cv
import serial
import numpy as np 
#Help from here
#https://www.tutorialspoint.com/how-to-create-a-black-image-and-a-white-image-using-opencv-python

com_port = 'COM0'
#com_port = '/dev/ttyACM0'
arduino = serial.Serial(port=com_port, baudrate=9600, timeout=0.1)
webcam = cv.VideoCapture(0)
#cap = cv.VideoCapture('sample_images/test1.mp4')
#patronus_options = ['shark', 'croc', 'dragon', 'eagle', 'fox', 'giraffe', 'tiger']
patronus_options = [
    "butterfly",
    "cat",
    "cheetah",
    "doe",
    "dog",
    "eagle",
    "elephant",
    "fox",
    "giraffe",
    "horse",
    "lion",
    "otter",
    "owl",
    "phoenix",
    "rabbit",
    "stag",
    "tiger",
    "wisps",
    "wisps_2",
    "wolf"
]



def patronus(still, patronus_name):
    
    #patronus_name = patronus_options[2]
    vid = 'sample_images/' + patronus_name + '.mp4'
    cap = cv.VideoCapture(vid)
    ret2 = True
    while (ret2):
        #read in a frame from the webcam
        #ret, still = webcam.read()
        ret2, still2 = cap.read()
        if (ret2):
            still2 = cv.resize(still2, (still.shape[1], still.shape[0]))
            output = cv.addWeighted(still, .9, still2, .9, 0)
            #output = cv.resize(output, (output.shape[1]*2, output.shape[0]*2))
            output = cv.flip(output, flipCode=0)
            cv.imshow("", output)
            key = cv.waitKey(25)
        else:
            key = ord('s')
            cap.release()
            #cv.destroyAllWindows()
            return
    



def write_serial(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data



print("Starting")


height = 720
width = 480
#height = 1880
#width = 1040
#height = 3760
#width = 2080
if __name__=='__main__':
    #black_image = np.zeros((width,height, 3), dtype = np.uilnt8)
    patronus_options_working = patronus_options.copy()
    
    black_image = np.ones((width,height, 3), dtype = np.uint8)
    #patronus()
    cv.imshow("", black_image)
    while True:
        data = arduino.readline()
        #print(data)
        message = data.decode()
        if len(message) > 1:
            print(message)
            print(type(message))
        #if any meaningful button pressed on IR receiver 
        if len(message) > 2 and len(message) < 20:
            patronus_name = random.choice(patronus_options_working)
            patronus_options_working.remove(patronus_name)
            patronus(black_image, patronus_name)
            if patronus_options_working == []:
                patronus_options_working = patronus_options.copy()
            cv.imshow("", black_image)
            
    cv.destroyAllWindows()
        

        
            
            
