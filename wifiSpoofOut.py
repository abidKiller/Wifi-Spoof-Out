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

stop_animation=False

def one_spoof():
    global network
    os.system("clear||cls")

    print('{}ONE {}Spoof Out{}'.format(Color.RED,Color.YELLOW,Color.END))

    thread=threading.Thread(target=PrintUtils.scanning_animation,args=(PrintUtils,'SCAN',))
    thread.daemon=True
    thread.start()

    try:
        scanner=Scanner()
        scanner.scan_neighbours()
    except:
        print('ERROR : Could not scan netwrok'.format(Color.RED,Color.YELLOW,Color.END))

    scanner.stop_animation=True
    
    online_ips=network.get_online_ips()
    vendors=network.resolve_mac()

    print('{}Online Devices: {}'.format(Color.YELLOW,Color.END))
        
    print('{}             IP                      MAC                     VENDOR'.format(Color.BLUE,Color.END))
    print('    __________________________________________________________________________\n')
    i=0
    for host in zip(online_ips,scanner.host_list[1],vendors):
            
            print('{}[{}{}{}]      {}{}         {}         {}{}'.format(Color.GREEN,Color.RED,i,Color.GREEN,Color.YELLOW,host[0],host[1],host[2],Color.END))    
            i=i+1

def multiple_spoof():
    pass
def all_spoof():
    pass


def one_limit():
    pass

def main_loop():
    PrintUtils.heading()
    global network
    network=Network()
    try:
        while True:
             
            PrintUtils.menu()
            choice =input()

            if choice.upper() == 'E' or choice.upper() == 'EXIT':
                print('\n{}Have great day bruv'.format(Color.GREEN))
                raise SystemExit
            elif choice == 'O'or choice.upper() == 'O':
                one_spoof()
            elif choice == 'M'or choice.upper() == 'M':
                multiple_spoof()
            elif choice == 'A'or choice.upper() == 'A':
                all_spoof()
            elif choice.upper() == 'CLEAR':
                os.system("clear||cls")
            PrintUtils.heading()   
            
            

    except KeyboardInterrupt:
        print('\n{}Have great day bruv'.format(Color.GREEN))

if __name__ == "__main__":
    try:
        if os.geteuid()!=0 :
            print("\n"+"{}ERROR: RUN AGAIN WITH ROOT PRIVILEGES{}\n\t\t\t\t\tUSE: {}sudo wifiKicker.py ".format(Color.RED,Color.YELLOW,Color.GREEN,Color.END).center(153))
            exit()
    except:
        pass #for windows

    init()  # for colorama
   
    main_loop() # main program loop
    
    






