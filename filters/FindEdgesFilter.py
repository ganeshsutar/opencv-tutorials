import numpy
from VConvolutionFilter import *

class FindEdgesFilter(VConvolutionFilter):
    def __init__(self):
        kernel = numpy.array([
            [-1, -1, -1],
            [-1,  8, -1],
            [-1, -1, -1]
        ])
        VConvolutionFilter.__init__(self, kernel)
