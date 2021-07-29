#!/usr/bin/env python3

import os
import sys
import math
import traceback
import threading
import optparse
from time import sleep
from printUtils import color
import colorama

try:
    if os.geteuid()!=0 :
        print("\n{}ERROR: RUN AGAIN WITH ROOT PRIVILEGES\n\t{}USE: {}sudo wifiKicker.py ".format(color.RED,color.YELLOW,color.GREEN))
except:
    pass #for windows



if __name__ == "__main__":
    print("\n{}ERROR: RUN AGAIN WITH ROOT PRIVILEGES\n\t{}USE: {}sudo wifiKicker.py{} ".format(color.RED,color.YELLOW,color.GREEN,color.END))
