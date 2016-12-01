"""
"""

import cv2
import numpy as np

class CascadeClassifier:
    def __init__(self, xmlfile, callback=None):
        self.cascade = cv2.CascadeClassifier(xmlfile)
        self.callback = callback

    def filter(self, frame):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2GRAY)
        faces = self.cascade.detectMultiScale(gray_frame, 1.3, 5)
        for (x,y,w,h) in faces:
            if(self.callback != None):
                self.callback(frame[y:y+h, x:x+w])
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0,0), 1)
        return frame
