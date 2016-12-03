import util
import cv2
import numpy

class BGRFuncFilter(object):
    def __init__(self, vFunc = None, bFunc = None, gFunc = None, rFunc = None, dtype = numpy.uint8):
        length = numpy.iinfo(dtype).max + 1
        self.bLookupArray = util.createLookupArray(util.createCompositeFunc(bFunc, vFunc), length)
        self.gLookupArray = util.createLookupArray(util.createCompositeFunc(gFunc, vFunc), length)
        self.rLookupArray = util.createLookupArray(util.createCompositeFunc(rFunc, vFunc), length)

    def filter(self, frame):
        """Apply the filter with a BGR source"""
        b,g,r = cv2.split(frame)
        b = util.applyLookupArray(self.bLookupArray, b)
        g = util.applyLookupArray(self.gLookupArray, g)
        r = util.applyLookupArray(self.rLookupArray, r)
        cv2.merge([b,g,r], frame)
        return frame


class BGRCurveFilter(BGRFuncFilter):
    def __init__(self, vPoints = None, bPoints = None, gPoints = None, rPoints = None, dtype = numpy.uint8):
        BGRFuncFilter.__init__(self,
            util.createCurveFunc(vPoints),
            util.createCurveFunc(bPoints),
            util.createCurveFunc(gPoints),
            util.createCurveFunc(rPoints),
            dtype)
