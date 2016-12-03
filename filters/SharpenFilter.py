from VConvolutionFilter import *
import numpy

class SharpenFilter(VConvolutionFilter):
    def __init__(self):
        kernel = numpy.array([
            [-1, -1, -1],
            [-1,  9, -1],
            [-1, -1, -1]
        ])
        VConvolutionFilter.__init__(self, kernel)
