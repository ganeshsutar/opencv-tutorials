import cv2
import numpy

class CMVColorSpace:
    def filter(self, frame):
        b,g,r = cv2.split(frame)
        cv2.max(b, g, b)
        cv2.max(b, r, b)
        cv2.merge((b,g,r), frame)
        return frame
