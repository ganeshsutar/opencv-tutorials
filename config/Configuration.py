import ConfigParser
import logging
import os

def load_props(filename):
    logging.debug('Loading properties from file %s', filename)
    config = ConfigParser.SafeConfigParser()
    config.read(filename)
    props = {}
    for section in config.sections():
        for key, value in config.items(section, vars={'pathsep': os.path.sep}):
            if key == 'pathsep':
                continue
            nkey = '%s.%s' % (section, key)
            props[nkey] = value
            logging.debug('Found %s --> %s', nkey, value)
    logging.info('Configuration loaded %s', filename)
    return props
