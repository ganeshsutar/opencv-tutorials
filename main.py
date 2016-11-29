#! /usr/bin/python

import logging
import cv2
import filters
import util
import cairo

class DisplayHudInfo:
    def __call__(self, surface):
        ctx = cairo.Context(surface)
        ctx.select_font_face('Consolas')
        ctx.set_font_size(12)
        ctx.set_source_rgb(0,1.0,1.0)
        ctx.move_to(2,12)
        ctx.show_text('version 0.0.1.172')

def main():
    rgbConverter = filters.ColorConverter(cv2.COLOR_BGR2RGBA)
    hud_filter = filters.CairoSurface(DisplayHudInfo())
    bgrConverter = filters.ColorConverter(cv2.COLOR_RGBA2BGR)
    chain = filters.Composite([rgbConverter, hud_filter, bgrConverter])
    rt = util.RealTimeVideoStream(chain)
    rt.run()

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
