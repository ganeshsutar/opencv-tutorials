from VConvolutionFilter import *
import numpy

class EmbossFilter(VConvolutionFilter):
    def __init__(self):
        kernel = numpy.array([
            [-2, -1, 0],
            [-1, 1, 1],
            [0, 1, 2]
        ])
        VConvolutionFilter.__init__(self, kernel)
