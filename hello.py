#!/usr/bin/env python3

import sys
import os

try:
    import dbus
except ImportError:
    print('ImportError: missing dbus!')

print('Dumping sys.path entries')
if __name__ == '__main__':
    print('library path= (%s)' % sys.path)

    for directory in sys.path:
        if os.path.isdir(directory):
            dir_listing = os.listdir(directory)
            for d in dir_listing:
                print('%s/%s' % (directory, d))
        else:
            print('sys.path entry %s not a directory' % directory)

    print('Hello travis-ci! %s' % str(sys.version_info))
