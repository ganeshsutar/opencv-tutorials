import cv2
import numpy

class RCColorSpace:
    def filter(self, frame):
        b,g,r = cv2.split(frame)
        cv2.addWeighted(b, 0.5, g, 0.5, 0, b)
        cv2.merge((b, b, r), frame)
        return frame
