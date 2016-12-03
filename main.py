#! /usr/bin/python

import argparse
import logging
from datetime import datetime
import logging

parser = argparse.ArgumentParser(
    description = 'zen'
)
parser.add_argument('-v', '--verbose', help='Set the logging level to DEBUG', action='store_true')
parser.add_argument('-c', '--fourcc', help='FourCC to be used for video writing')

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

width = 1280
height = 738

def get_input_random():
    return io.RandomInput(width, height, True)

def get_input():
    return cv2.VideoCapture('.\\videos\\cut.mp4')

def get_output():
    n = datetime.utcnow()
    current_filename = '.\\videos\\cap-' + n.strftime('%Y%m%d-%H%M%S') + '.avi'
    if args.fourcc:
        logging.info("Using 4CC = '%s'", args.fourcc)
        if len(args.fourcc) == 4:
            fourcc = cv2.cv.CV_FOURCC(*args.fourcc)
        else:
            logging.info('FourCC gives does not have 4 characters. Please choose the output coded')
            fourcc = -1
    else:
        fourcc = cv2.cv.CV_FOURCC(*'I420')
    writer = cv2.VideoWriter(current_filename, fourcc, 30.0, (width, height))
    return writer

if __name__ == "__main__":
    rt = util.RealTimeVideoStream(get_input(), get_output(), None)
    rt.run()
