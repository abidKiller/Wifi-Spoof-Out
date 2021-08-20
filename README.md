# Wifi-Spoof-Out

Remove Unawanted devices from your wifi network using the concept of ARP-SPOOFING

# Screenshots
<img src="https://github.com/abidKiller/Wifi-Spoof-Out/blob/main/doc/main.JPG" alt="drawing" width="800"/>
<img src="https://github.com/abidKiller/Wifi-Spoof-Out/blob/main/doc/onespoof.JPG" alt="drawing" width="800"/>

# THEORY
<img src="https://github.com/abidKiller/Wifi-Spoof-Out/blob/main/doc/arp-spoofing-diagram.png" alt="drawing" width="800"/>

1. At first Node 1 gets mac address of neighbour Nodes
2. Then sends Arp packets to target to believe that Node 1's mac address is router's mac address .
3. Thus, targets iptable gets messed up and can't use the network as it can't access the router
4. this concept is also used in MITM(Man in the Middle Attack)

# Installation 
```
git clone https://github.com/abidKiller/Wifi-Spoof-Out.git
cd  Wifi-Spoof-Out
pip install Requirements.txt

```
# Run
```
python wifiSpoofOut.py
```
# License

Copyright (c) 2020-2021 by [Abid Ahsan Samin](mailto:abidahsan@iut-dhaka.edu). Some rights reserved.

Wifi-Spoof-Out is under the terms of the [MIT License](https://www.tldrlegal.com/l/mit), following all clarifications stated in the [license file]().




