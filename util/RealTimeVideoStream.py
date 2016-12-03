"""
A class to capture and save a realtime video with the given filter chain
"""

import cv2
from datetime import datetime
import logging

class RealTimeVideoStream:
    def __init__(self, input, output, chain = None):
        assert input != None, "Input cannot be None"
        # assert output != None, "Output cannot be None"

        self.input = input
        self.output = output
        self.chain = chain

    def run(self):
        logging.debug('Started filtering ...')
        while(self.input.isOpened()):
            # logging.debug('Getting frame from input')
            ret, frame = self.input.read()
            if ret == True:
                if self.chain != None:
                    frame = self.chain.filter(frame)
                # logging.debug('Writing frame to output')
                if( self.output != None ):
                    self.output.write(frame)
                cv2.imshow('frame', frame)
                if cv2.waitKey(1) & 0xff == ord('q'):
                    break
            else:
                break
        logging.debug('Input Opened %s', str(self.input.isOpened()))
        self.input.release()
        if(self.output != None):
            self.output.release()
        cv2.destroyAllWindows()
