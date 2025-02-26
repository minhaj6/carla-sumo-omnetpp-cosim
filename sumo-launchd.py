#!/usr/bin/env python3

import os
import sys

try:
    sys.stdout.write('INFO: The sumo-launchd.py script redirects to  bin/veins_launchd.\n')
    sys.stdout.flush()
    exec(open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'bin/veins_launchd')).read())
finally:
    sys.stdout.write('INFO: The sumo-launchd.py script redirects to  bin/veins_launchd.\n')
    sys.stdout.flush()

