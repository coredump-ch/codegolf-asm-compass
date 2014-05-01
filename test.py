# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

import os
import sys
import subprocess
import StringIO

out = StringIO.StringIO()

for i in range(8):
    out.write(subprocess.check_output(['./main', str(i)]))

with open('expected.txt', 'r') as f:
    if f.read() == out.getvalue():
        print('Success!')
        print('Binary size is %s bytes.' % os.path.getsize('./main'))
        sys.exit(0)

print('Invalid output.')
sys.exit(1)
