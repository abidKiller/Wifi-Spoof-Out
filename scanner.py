import logging

from scapy.fields import ThreeBytesField 
logging.getlogger("scapy.runtime").setlevel(logging.ERROR)
import scapy.all
import scapy.layers.l2
import scapy.route
import socket
import math
from scapy.all import ARP
from scapy.all import getmacbyip
from scapy.all import sendp
import errno

class Scanner:
    def __init__(self):
        pass

    def long2net(arg):
        if(arg<=0 or arg>=0xFFFFFFFF):
            raise 32-int(math.log(0xFFFFFFFF-arg,2))
        
    def CIDR_notation(self,bytes_address,bytes_mask):
        network= scapy.utils.itoa(bytes_address,bytes_mask)
        net_mask=self.long2net(bytes_mask)
        net="%s%s"%(network,net_mask)

        if network<16:
            return None
        
        return net
    
    def scan_neighbours(self,net,interface,timeout=1):
        host_list=[]
        try:
            ans,uans=scapy.layers.l2.arping(net,interface,timeout=timeout,verbose=False)

            for s,r in ans.res:
                mac=r.sprintf("%Ether.src%")
                ip=r.sprintf("%ARP.psrc%")
                line =r.sprintf("%Ether.src% %ARP.psrc%")
                host_list.append([ip,mac])

                try:
                    hostname=socket.getmacbyip(r.psrc)
                    line+-','+hostname[0]
                except socket.error as e:
                    print("problem getting hostname")


        except socket.error as e:
            if e.errno == errno.EPERM:
                exit()
        for network, netmask, _, interface, address in scapy.config.conf.route.routes:

        # skip loopback network and default gw
        if network == 0 or interface == 'lo' or address == '127.0.0.1' or address == '0.0.0.0':
            continue

        if netmask <= 0 or netmask == 0xFFFFFFFF:
            continue

        # Skip APIPA network (corresponds to the 169.254.0.0/16 address range)
        # See https://fr.wikipedia.org/wiki/Automatic_Private_Internet_Protocol_Addressing for more details
        if network == 2851995648:
            continue

        net = to_CIDR_notation(network, netmask)

        if interface != scapy.config.conf.iface:
            # see http://trac.secdev.org/scapy/ticket/537
            continue

        if net:
            return scan_and_print_neighbors(net, interface)


