import logging
import cv2
import os

class DirectoryDb:
    def __init__(self, baseDirectory):
        self.baseDirectory = baseDirectory
        self.persons = []
        self.labels = []
        self.images = []

    def load(self):
        self.persons = [dirname for dirname in os.listdir(self.baseDirectory) if os.path.isdir(os.path.join(self.baseDirectory, dirname))]
        self.labels = []
        self.images = []
        logging.debug('Persons: %s', self.persons)
        for idx, person in enumerate(self.persons):
            personImageDir = os.path.join(self.baseDirectory, person)
            logging.debug('Person Image Directory: %s', personImageDir)
            files = os.listdir(personImageDir)
            for filename in files:
                filepath = os.path.join(self.baseDirectory, person, filename)
                self.images.append(cv2.imread(filepath, cv2.IMREAD_GRAYSCALE))
                self.labels.append(idx)
