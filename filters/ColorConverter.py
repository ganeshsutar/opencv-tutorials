import cv2
from BasicFilter import BasicFilter

class ColorConverter(BasicFilter):
    def __init__(self, cv2_ColorConverterCode):
        self.code = cv2_ColorConverterCode

    def filter(self, frame):
        nframe = cv2.cvtColor(frame, self.code)
        return nframe
