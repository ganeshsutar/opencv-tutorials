from BGRFuncFilter import BGRCurveFilter
import numpy

class BGRProviaCurveFilter(BGRCurveFilter):
    def __init__(self, dtype = numpy.uint8):
        BGRCurveFilter.__init__(self,
            bPoints = [(0,0),(35,25),(205,227),(255,255)],
            gPoints = [(0,0),(27,21),(196,207),(255,255)],
            rPoints = [(0,0),(59,54),(202,210),(255,255)],
            dtype = dtype)
