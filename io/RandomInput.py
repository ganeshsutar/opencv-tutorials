import numpy
import os

class RandomInput:
    def __init__(self, width=640, height=480, colored = False):
        self.width = width
        self.height = height
        self.colored = colored

    def open(self):
        pass

    def release(self):
        pass

    def isOpened(self):
        return True

    def read(self):
        totalBytes = self.width * self.height
        if self.colored:
            totalBytes *= 3
        randomByteArray = bytearray(os.urandom(totalBytes))
        flatArray = numpy.array(randomByteArray)
        if self.colored:
            return (True, flatArray.reshape(self.height, self.width, 3))
        else:
            return (True, flatArray.reshape(self.height, self.width))
