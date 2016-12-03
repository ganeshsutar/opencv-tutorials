import scipy.interpolate
import numpy

def createCurveFunc( points ):
    """Returns a function derived from control points."""
    if points is None:
        return None
    numPoints = len(points)
    if numPoints < 2:
        return None
    xs, ys = zip(*points)
    if numPoints < 4:
        kind = 'linear'
    else:
        kind = 'cubic'
    return scipy.interpolate.interp1d(xs, ys, kind, bounds_error = False)

def createLookupArray( func , length = 256):
    """Return a lookup array for whole-number inputs to be function.

    The lookup values are clamped to [0, length-1].
    """
    if func is None:
        return None
    lookupArray = numpy.empty(length)
    i = 0
    while i < length:
        func_i = func(i)
        lookupArray[i] = min(max(0, func_i), length - 1)
        i += 1
    return lookupArray

def applyLookupArray(lookupArray, frame):
    if lookupArray is None:
        return None
    return lookupArray[frame]

def createCompositeFunc( func0, func1 ):
    """Return a composite of two function"""
    if func0 is None:
        return None
    if func1 is None:
        return None
    return lambda x: func0(func1(x))

def createFlatView(array):
    """Return a 1D view of an array of any dimensionality"""
    flatView = array.view()
    flatView.shape = array.size
    return flatView
