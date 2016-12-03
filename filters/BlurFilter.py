import cv2

class BlurFilter:
    """A Blur Filter with a k-pixel radius"""
    def __init__(self, pixels = 2):
        self.pixels = pixels

    def filter(self, frame):
        return cv2.medianBlur(frame, self.pixels)
