#!/usr/bin/env python3

import sys

try:
    import dbus
except:
    print('missing dbus!')

if __name__ == '__main__':
    print('Hello travis-ci! %s' % str(sys.version_info))
