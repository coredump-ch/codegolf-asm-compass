# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import sys
import subprocess
import random

COMPASS = (
    '   _N_\n' +
    '  /   \\\n' +
    'W|  .  |E\n' +
    ' |     |\n' +
    '  \\_ _/\n' +
    '    S\n'
)


def compass(direction):
    return {
        0: lambda x: x[:11] + "|" + x[12:],
        1: lambda x: x[:20] + "/" + x[21:],
        2: lambda x: x[:20] + "_" + x[21:],
        3: lambda x: x[:30] + "\\" + x[31:],
        4: lambda x: x[:38] + "|" + x[39:],
        5: lambda x: x[:28] + "/" + x[29:],
        6: lambda x: x[:18] + "_" + x[19:],
        7: lambda x: x[:18] + "\\" + x[19:]
    }[direction](COMPASS)

short = False
if '--short' in sys.argv:
    short = True
    sys.argv.remove('--short')

if len(sys.argv) == 1:
    path = './main'
elif len(sys.argv) == 2:
    path = sys.argv[2]
else:
    print('Usage: python test.py [path] [--short]')
    sys.exit(-1)

args = range(8)
random.shuffle(args)
size = os.path.getsize('./main')
for i in args:
    try:
        output = subprocess.check_output([path, str(i)])
        if output != compass(i):
            print('Invalid output.')
            sys.exit(1)
    except subprocess.CalledProcessError as e:
        print('Error calling binary with argument %d: %s' % (i, e))
        sys.exit(-1)

if short:
    print(size)
else:
    print('Success!')
    print('Binary size is %s bytes.' % size)
