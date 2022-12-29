
import uuid
print("The MAC adress in formatted way is :", end="")
print(':'.join(['{:02x}' . format ((uuid.getnode() >> ele)& 0xff)
for ele in range(0,8*6,8)][::-1]))  #8*6 is 8bits and 6parts with range 00 to ff

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(s)

"""import ifaddr
adapters=ifaddr.get_adapters()

for adapter in adapters():
    print("IPs of network adapter " + adapter.nice_name)
    if adapter.ips:
        for ip in adapters.IPs:
            print(" %s/%s" & (ip.ip,ip.network_prefix))
        else:
            print("no IPs configured")

import psutil

network_stats=psutil.net_io_counters(pernic=False)
bytes_sent =getattr(network_stats,'bytes_sent')
bytes_recv =getattr(network_stats,'bytes_recv')
print("Bytes Sent= {0}" | "Bytes Received = {1}" .format )"""


'''import socket
import subprocess
import sys

from datetime import datetime
subprocess.call('clear',shell=True)

remoteServer=input("Enter a remote host to scan: ")
remoteServerIP=socket.gethostbyname(remoteServer)

print("_"*60)
print("Please wait,scanning remote host",remoteServerIP)
print("_"*60)

t1=datetime.now()

try:
    for port in range(1,5000):
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result=sock.connect_




import scapy.all as scapy
request=scapy.ARP()
from scapy.all import *
my_frame= Ether() /IP()
print(my_frame)
print(my_frame.show())'''


from scapy.all import*
s= IP(dst='google.com')/ICMP()
print(s.show())

a=IP(tt1=10)
print(a)
print(a.src)
a.dst="192.168.1.1"
print(a)
print(a.src)



