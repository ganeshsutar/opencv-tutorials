#! /usr/bin/python

import cv2
import argparse
import logging

parser = argparse.ArgumentParser(description="Feature Matchers with ORB")
parser.add_argument('-v', '--verbose', help='Set logging level to DEBUG', action='store_true')
parser.add_argument('image', help='Path of the image you want to see')

args = parser.parse_args()
if args.verbose:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

logging.debug('Show information: %s', args.image)

img = cv2.imread(args.image, 0)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

logging.debug(done)
