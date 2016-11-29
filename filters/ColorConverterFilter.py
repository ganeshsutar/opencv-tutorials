import cv2
from BasicFilter import BasicFilter

class ColorConverterFilter(BasicFilter):
    def __init__(self, cv2_ColorConverterCode):
        self.code = cv2_ColorConverterCode

    def filter(self, frame):
        converter_frame = cv2.cvtColor(frame, self.code)
        return converter_frame
