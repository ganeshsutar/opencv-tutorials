#! /usr/bin/python

import argparse
import logging

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
import db
import cv2
import filters
import util

if __name__ == "__main__":
    # grayFilter = filters.ColorConverter(cv2.COLOR_BGR2GRAY)
    # backFilter = filters.ColorConverter(cv2.COLOR_GRAY2BGR)
    # composite = filters.Composite([grayFilter, backFilter])
    # rt = util.RealTimeVideoStream(composite)
    # rt.run()
    print config.props
    print db.conn.getPersons()
