"""
A filter than run all the given filter in order.
"""

from BasicFilter import BasicFilter

class Composite(BasicFilter):
    def __init__(self, filters):
        self.filters = filters

    def filter(self, frame):
        for f in self.filters:
            frame = f.filter(frame)
        return frame
