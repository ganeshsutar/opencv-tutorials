from BGRFuncFilter import BGRCurveFilter
import numpy

class BGRCrossProcessCurveFilter(BGRCurveFilter):
    def __init__(self, dtype = numpy.uint8):
        BGRCurveFilter.__init__(self,
            bPoints = [(0,20),(255,235)],
            gPoints = [(0,0),(56,39),(208,226),(255,255)],
            rPoints = [(0,0),(56,22),(211,255),(255,255)],
            dtype = dtype)
