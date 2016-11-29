import cv2
import numpy as np

class PerspectiveTransformer:
    def __init__(self, fromPoints, toPoints):
        self.transformer = cv2.getPerspectiveTransform(fromPoints, toPoints)

    def filter(self, frame):
        rows, cols, d = frame.shape
        nframe = cv2.warpPerspective(frame, self.transformer, (cols, rows))
        return nframe
