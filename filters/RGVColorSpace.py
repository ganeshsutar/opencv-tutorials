import cv2
import numpy

class RGVColorSpace:
    def filter(self, frame):
        b,g,r = cv2.split(frame)
        cv2.min(b, g, b)
        cv2.min(b, r, b)
        cv2.merge((b,g,r), frame)
        return frame
