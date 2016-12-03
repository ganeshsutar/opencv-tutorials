import VFuncFilter
import util

class VCurveFilter(VFuncFilter):
    def __init__(self, vPoints, dtype = numpy.uint8):
        VFuncFilter.__init__(self, util.createCurveFunc(vPoints), dtype)
