import cv2
import numpy as np

class AffineTransformer:
    def __init__(self, fromPoints, toPoints):
        self.transformer = cv2.getAffineTransform(fromPoints, toPoints)

    def filter(self, frame):
        rows, cols, d = frame.shape
        nframe = cv2.warpAffine(frame, self.transformer, (cols, rows))
        return nframe
