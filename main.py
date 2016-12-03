#! /usr/bin/python

import argparse
import logging
from datetime import datetime

parser = argparse.ArgumentParser(
    description = 'zen'
)
parser.add_argument('-v', '--verbose', help='Set the logging level to DEBUG', action='store_true')

args = parser.parse_args()

if (args.verbose):
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

import config
import cv2
import filters
import util
import io

def get_input():
    return io.RandomInput(640, 480, True)

def get_output():
    n = datetime.utcnow()
    current_filename = '.\\videos\\cap-' + n.strftime('%Y%m%d-%H%M%S') + '.avi'
    fourcc = cv2.cv.CV_FOURCC(*'I420')
    return cv2.VideoWriter(current_filename, fourcc, 20.0, (640, 480))


if __name__ == "__main__":
    chain = filters.CMVColorSpace()
    rt = util.RealTimeVideoStream(get_input(), get_output(), chain)
    rt.run()
