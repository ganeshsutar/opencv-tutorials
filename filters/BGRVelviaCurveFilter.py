from BGRFuncFilter import BGRCurveFilter
import numpy

class BGRVelviaCurveFilter(BGRCurveFilter):
    def __init__(self, dtype = numpy.uint8):
        BGRCurveFilter.__init__(self,
            vPoints = [(0,0),(128,118),(221,215),(255,255)],
            bPoints = [(0,0),(25,21),(122,153),(165,206),(255,255)],
            gPoints = [(0,0),(25,21),(95,102),(181,208),(255,255)],
            rPoints = [(0,0),(41,28),(183,209),(255,255)],
            dtype = dtype)
