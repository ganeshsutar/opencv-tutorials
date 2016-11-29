#! /usr/bin/python

import logging
import cv2
import filters
import util
import cairo
import numpy as np

def main():
    # All frame will be in RGBA format
    rgbConverter = filters.ColorConverter(cv2.COLOR_BGR2RGBA)
    cascade = filters.CascadeClassifier(".\\data\\face_haar.xml")
    bgrConverter = filters.ColorConverter(cv2.COLOR_RGBA2BGR)
    chain = filters.Composite([rgbConverter, cascade, bgrConverter])
    rt = util.RealTimeVideoStream(chain)
    rt.run()

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
