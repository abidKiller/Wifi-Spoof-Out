from urllib.request import urlopen,Request
from urllib.error import URLError
import scapy.all
from scapy.all import ARP,ICMP,IP,sr1
from scanner import Scanner
from scapy.arch import get_if_hwaddr
from printUtils import Color
import math

class Network:
    def __init__(self):
        self.online_IPs=None
        self.default_interface=self.get_default_interface()
        self.default_gateway_IP= self.get_gateway_IP()
        self.default_getway_mac_set=None
        self.default_interface_mac=self.get_default_interface_mac()
        scanner=Scanner()
        self.host_list=None
        self.vendors=None

    def resolve_mac(self):
        try:
            # send request to macvendors.co
            for host in self.host_list: 
                url = "http://macvendors.co/api/vendorname/"
                request = Request(url +self.host_list[1], headers={'User-Agent': "API Browser"})
                response = urlopen(request)
                vendor = response.read()
                vendor = vendor.decode("utf-8")
                vendor = vendor[:25]
                self.vendors.append(vendor)
            return self.vendors

        except KeyboardInterrupt:
            exit()
        except:
            return "N/A"
    def check_internet(self):
        try:
            urlopen('https://github.com',timeout=3)
            return True
        except URLError as e:
            return False
    def get_default_interface(self):
        def long2net(arg):
            if (arg <= 0 or arg >= 0xFFFFFFFF):
                raise ValueError("illegal netmask value", hex(arg))
            return 32 - int(round(math.log(0xFFFFFFFF - arg, 2)))
        def to_CIDR_notation(bytes_network, bytes_netmask):
            network = scapy.utils.ltoa(bytes_network)
            netmask = long2net(bytes_netmask)
            net = "%s/%s" % (network, netmask)
            if netmask < 16:
                return None
            return net
        for network,net_mask,_,interface,address,_ in scapy.config.conf.route.routes:
            if network==0 or interface=='lo' or address=='127.0.0.1' or address=='0.0.0.0':
                continue
            if net_mask < 0 or net_mask == 0xFFFFFFFF:
                continue
            net=to_CIDR_notation(network,net_mask)
            if interface !=scapy.config.conf.iface :
                continue
            if net:
                return interface

    def get_default_interface_mac(self):
        try:
            self.default_interface=self.get_default_interface()
            self.default_interface_mac= get_if_hwaddr(self.default_interface)
        except :
            print('\n{}ERROR :{}Could not Obtain {}Default interface MAC address \n'.format(Color.RED,Color.YELLOW,Color.BLUE))
            print('{}ENTER MANUALLY ({}e.g. MM:MM:MM:SS:SS:SS): '.format(Color.YELLOW,Color.GREEN))
            self.default_gateway_mac=input()
            self.default_gateway_mac_set=True
        
        return self.default_interface_mac


    def get_gateway_IP(self):
        try:
            gateway_packet=sr1(IP(dst="google.com",ttl=0)/ICMP()/ "XXXXXXXXXXX", verbose=False)
            return gateway_packet.src
        except:
            print("\n{}ERROR:{}Could not obtain Gateway IP\n".format(Color.RED, Color.END))
            header = ('{}ENTER MANUALLY {}(e.g. 192.168.0.8): '.format(Color.YELLOW,Color.GREEN))
            gateway_ip=input(header)
            return gateway_ip
            

    def get_online_IPs(self):
        if not self.default_gateway_mac_set:
            self.default_getway_mac_set=""
        
        self.online_IPs=[]
        for host in self.host_list:
            self.online_IPs.append(host[0])
            if not self.default_gateway_mac_set:
                if host[0] == self.default_gateway_IPs:
                    self.default_gateway_mac=host[1]
        if not self.default_gateway_mac_set and self.default_gateway_mac==0:
            print('\n{}ERROR :{}Could not Obtain {}gateway MAC address \n'.format(Color.RED,Color.YELLOW,Color.BLUE))
            print('{}ENTER MANUALLY ({}e.g. MM:MM:MM:SS:SS:SS): \r'.format(Color.YELLOW,Color.GREEN))
            self.default_gateway_mac=input()
            self.default_gateway_mac_set=True
                    
if __name__ == '__main__':
    net=Network()
    print(net.default_gateway_IP)





