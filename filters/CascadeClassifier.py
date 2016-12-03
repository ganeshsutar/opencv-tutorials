"""
"""

import cv2
import numpy as np
import logging

class CascadeClassifier:
    def __init__(self, xmlfile, callback=None):
        logging.debug('Creating Cascade Classifier %s', xmlfile)
        self.cascade = cv2.CascadeClassifier(xmlfile)
        self.callback = callback
        logging.debug('Cascade Classifier Created')

    def filter(self, frame):
        # logging.debug('Detecting faces')
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2GRAY)
        faces = self.cascade.detectMultiScale(gray_frame, 1.3, 5)
        # logging.debug('Found Faces: %s', str(faces))
        for (x,y,w,h) in faces:
            if(self.callback != None):
                self.callback(frame[y:y+h, x:x+w])
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0,0), 1)
        return frame
