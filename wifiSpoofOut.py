#!/usr/bin/env python3

import os
import sys
import math
import traceback
import threading
import optparse
from time import sleep
from printUtils import Color
from colorama import init
from printUtils import heading

try:
    if os.geteuid()!=0 :
        print("\n"+"{}ERROR: RUN AGAIN WITH ROOT PRIVILEGES{}\n\t\t\t\t\tUSE: {}sudo wifiKicker.py ".format(Color.RED,Color.YELLOW,Color.GREEN,Color.END).center(153))
        exit()
except:
    pass #for windows



if __name__ == "__main__":

    init()
    

   
    heading()
    print('\nChoose an option from the menu:\n')
    
    print('\t\t{}[{}O{}]{} Spoof out {}ONE{} device'.format(Color.YELLOW,Color. RED, Color.YELLOW,Color. WHITE,Color.GREEN,Color.WHITE))
    
    print('\t\t{}[{}M{}]{} Spoof out {}MULTIPLE{} devices'.format(Color.YELLOW,Color. RED, Color.YELLOW,Color. WHITE,Color.GREEN,Color.WHITE))
    
    print('\t\t{}[{}A{}]{} Spoof Out {}ALL{} devices'.format(Color.YELLOW,Color. RED,Color. YELLOW,Color. WHITE,Color.GREEN,Color.WHITE))

    print('\t\t{}[{}L{}]{} Spoof Out {}Limit ONE{} device'.format(Color.YELLOW,Color. RED,Color. YELLOW,Color. WHITE,Color.GREEN,Color.WHITE))

    print('\n\t\t{}[{}E{}]{} Exit\n'.format(Color.YELLOW, Color.RED, Color.YELLOW, Color.WHITE))
