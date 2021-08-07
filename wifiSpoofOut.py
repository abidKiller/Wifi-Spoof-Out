#!/usr/bin/env python3

import os
import sys
import math
import traceback
import threading
import optparse
from time import sleep
from printUtils import PrintUtils
from printUtils import Color


from colorama import init
from scanner import Scanner
from spoof import Spoof
from network import Network

try:
    if os.geteuid()!=0 :
        print("\n"+"{}ERROR: RUN AGAIN WITH ROOT PRIVILEGES{}\n\t\t\t\t\tUSE: {}sudo wifiKicker.py ".format(Color.RED,Color.YELLOW,Color.GREEN,Color.END).center(153))
        exit()
except:
    pass #for windows


def one_spoof():
    pass
def multiple_spoof():
    pass
def all_spoof():
    pass

def main_loop():
    pass
def one_limit():
    pass

if __name__ == "__main__":
    
    init()
    PrintUtils.heading()
    PrintUtils.menu()
    main_loop()
    PrintUtils.scanning_animation(PrintUtils,'scan')
    






