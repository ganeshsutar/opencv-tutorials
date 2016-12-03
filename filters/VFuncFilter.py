import util
import numpy

class VFuncFilter(object):
    """A filter that applies a function to V (or all BGR)."""

    def __init__(self, vFunc = None, dtype = numpy.uint8):
        length = numpy.iinfo(dtype).max + 1
        self.vLookupArray = util.createLookupArray(vFunc, length)

    def filter(self, frame):
        """Apply the filter with a BGR or gray source"""
        rvar = util.createFlatView(frame)
        return util.applyLookupArray(self.vLookupArray, rvar)
