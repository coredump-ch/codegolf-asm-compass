# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

import os
import sys
import subprocess
import StringIO

out = StringIO.StringIO()

for i in range(8):
    try:
        output = subprocess.check_output(['./main', str(i)])
    except subprocess.CalledProcessError as e:
        print('Error calling binary with argument %d: %s' % (i, e))
        sys.exit(-1)
    out.write(output)

with open('expected.txt', 'r') as f:
    if f.read() == out.getvalue():
        print('Success!')
        print('Binary size is %s bytes.' % os.path.getsize('./main'))
        sys.exit(0)

print('Invalid output.')
sys.exit(1)
