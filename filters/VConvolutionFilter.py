import cv2

class VConvolutionFilter:
    def __init__(self, kernel):
        self.kernel = kernel

    def filter(self, frame):
        cv2.filter2D(frame, -1, self.kernel, frame)
        return frame
