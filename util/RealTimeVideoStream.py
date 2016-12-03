"""
A class to capture and save a realtime video with the given filter chain
"""

import cv2
from datetime import datetime

class RealTimeVideoStream:
    def __init__(self, input, output, chain = None):
        assert input != None, "Input cannot be None"
        assert output != None, "Output cannot be None"

        self.input = input
        self.output = output
        self.chain = chain

    def run(self):
        while(self.input.isOpened()):
            ret, frame = self.input.read()
            if ret == True:
                if self.chain != None:
                    frame = self.chain.filter(frame)
                self.output.write(frame)
                cv2.imshow('frame', frame)
                if cv2.waitKey(1) & 0xff == ord('q'):
                    break
            else:
                break
        self.input.release()
        self.output.release()
        cv2.destroyAllWindows()
