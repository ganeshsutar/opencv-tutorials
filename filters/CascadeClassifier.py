"""
"""

import cv2
import numpy as np

class CascadeClassifier:
    def __init__(self, xmlfile):
        self.cascade = cv2.CascadeClassifier(xmlfile)

    def filter(self, frame):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2GRAY)
        faces = self.cascade.detectMultiScale(gray_frame, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0,0), 1)
        return frame
