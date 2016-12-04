import cv2

class StrokeEdgesFilter:
    def __init__(self, blurKsize = 7, edgeKsize = 5):
        self.blurKsize = blurKsize
        self.edgeKsize = edgeKsize

    def filter(self, frame):
        blurredSrc = cv2.medianBlur(frame, self.blurKsize)
        graySrc = cv2.cvtColor(blurredSrc, cv2.COLOR_BGR2GRAY)
        cv2.Laplacian(graySrc, cv2.cv.CV_8U, graySrc, ksize = self.edgeKsize)
        normalizedInverseAlpha = (1.0/255) * (255 - graySrc)
        channels = cv2.split(frame)
        for channel in channels:
            channel[:] = channel * normalizedInverseAlpha
        cv2.merge(channels, frame)
        return frame
