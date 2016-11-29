"""
A class to capture and save a realtime video with the given filter chain
"""

import cv2
from datetime import datetime

class RealTimeVideoStream:
    def __init__(self, chain, resolution = (640, 480)):
        self.chain = chain
        self.current_filename = None
        self.resolution = resolution

    def new_capture(self):
        n = datetime.utcnow()
        self.current_filename = '.\\videos\\cap-' + n.strftime('%Y%m%d-%H%M%S') + '.avi'
        return self.current_filename

    def getFilename(self):
        return self.current_filename

    def run(self):
        self.new_capture()
        cap = cv2.VideoCapture(0)
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        out = cv2.VideoWriter(self.current_filename, fourcc, 20.0, self.resolution)
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                oframe = self.chain.filter(frame)
                out.write(oframe)
                cv2.imshow('frame', oframe)
                if cv2.waitKey(1) & 0xff == ord('q'):
                    break
            else:
                break
        cap.release()
        out.release()
        cv2.destroyAllWindows()
