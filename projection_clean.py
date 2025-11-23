import datetime
import os
import time
import random
import cv2 as cv
import serial
import numpy as np 
#Help from here
#https://www.tutorialspoint.com/how-to-create-a-black-image-and-a-white-image-using-opencv-python

#com_port = 'COM0'
#com_port = '/dev/ttyACM0'
#arduino = serial.Serial(port=com_port, baudrate=9600, timeout=0.1)
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
    "owl",
    "phoenix",
    "stag",
    "swirl",
    "tiger",
    "vortex",
    "wisps_1",
    "wolf"
]


def patronus(still):
    patronus_name = random.choice(patronus_options)
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
            cv.imshow("Show", output)
            key = cv.waitKey(42)
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



height = 1880
width = 1040
if __name__=='__main__':
    #black_image = np.zeros((width,height, 3), dtype = np.uint8)
    black_image = np.ones((width,height, 3), dtype = np.uint8)
    #patronus()
    cv.imshow("Show", black_image)
    while True:
        key = cv.waitKey(5)
        user_input = input()
        if len(user_input) <= 0:
            continue
        else:
            patronus(black_image)
            cv.imshow("Show", black_image)
    cv.destroyAllWindows()
        

        
            
            
