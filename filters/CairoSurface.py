"""
A filter that create a cairo surface and call the callback to draw using
cairo function and return again back to opencv frame.

**** REQUIRES RGB IMAGE ****
"""

import cv2
import cairo
import numpy as np
import logging
from BasicFilter import BasicFilter

logging.warn('CairoSurface requires RGBA color image')

def get_surface_fromRGBA(img):
    rows, cols, d = img.shape
    flat = img.flatten()
    surface = cairo.ImageSurface.create_for_data(flat,cairo.FORMAT_RGB24, cols,rows)
    return surface

def get_image_from_surface(surface):
    rows = surface.get_height()
    cols = surface.get_width()
    im = np.frombuffer(surface.get_data(),np.uint8)
    im.shape = (rows,cols,4)
    return im

class CairoSurface(BasicFilter):
    def __init__(self, callback):
        self.callback = callback

    def filter(self, frame):
        rgbSurface = get_surface_fromRGBA(frame)
        self.callback(rgbSurface)
        nframe = get_image_from_surface(rgbSurface)
        return nframe
