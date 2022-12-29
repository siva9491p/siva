'''from scapy.all import *

s= IP(dst='google.com')/ICMP()
print(s.show())
a=IP(tt1=10)
print(a)
print(a.src)
a.dst="192.168.1.1"
print(a)
print(a.src)

c=IP()/TCP()
print(c.show())

d=Ether()/IP()/TCP()
print(d.show())

e=IP()/TCP()/"GET/HTTP/1.0\r\n\r\n"
print(e.show())

j=a=Ether()/IP(dst="www.slash.org")/TCP()/"GET/index.html HTTP/1.0\n\n"
print(hexdump(j)'''



"""import psutil
import time

UPDATE_DELAY =1 # in seconds

def get_size(bytes):
    for unit in ['','K','M','G','T','P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes/=1024
        io=psutil.net_io_counters()
        bytes_sent,bytes_recv=io.bytes_sent,io.bytes_recv
while True:
    time.sleep(UPDATE_DELAY)
    io_2=psutil.net_io_counters()
    us,ds=io_2.bytes_sent,io_2.bytes_recv
    print(f"Upload: {get_size(io_2.bytes_sent)}   "
    f",Dowload: {get_size(io_2.bytes_recv)}     "
    f",Upload speed: {get_size(us/UPDATE_DELAY)}/s     "
    f",Dowload speed:{get_size(ds/UPDATE_DELAY)}/s         ",end="\r")
    bytes_sent,bytes_recv=io_2.bytes_sent,io_2.bytes_recv"""



import psutil
import time
import os
import pandas as pd

UPDATE_DELAY = 1 # in seconds

def get_size(bytes):
    """
    Returns size of bytes in a nice format
    """
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024

# get the network I/O stats from psutil on each network interface
# by setting `pernic` to `True`
io = psutil.net_io_counters(pernic = True) #pernic :: per NIC

while True:
    # sleep for `UPDATE_DELAY` seconds
    time.sleep(UPDATE_DELAY)
    # get the network I/O stats again per interface
    io_2 = psutil.net_io_counters(pernic = True)
    # initialize the data to gather (a list of dicts)
    data = []
    for iface, iface_io in io.items() :
        # new - old stats gets us the speed
        upload_speed, download_speed = io_2[iface].bytes_sent - iface_io.bytes_sent, io_2[iface].bytes_recv - iface_io.bytes_recv
        data.append({
            "iface": iface, "Download": get_size(io_2[iface].bytes_recv),
            "Upload": get_size(io_2[iface].bytes_sent),
            "Upload Speed": f"{get_size(upload_speed / UPDATE_DELAY)}/s",
            "Download Speed": f"{get_size(download_speed / UPDATE_DELAY)}/s",
        })
    # update the I/O stats for the next iteration
    io = io_2
    # construct a Pandas DataFrame to print stats in a cool tabular style
    df = pd.DataFrame(data)
    # sort values per column, feel free to change the column
    df.sort_values("Download", inplace=True, ascending=False)
    # clear the screen based on your OS
    os.system("cls") if "nt" in os.name else os.system("clear")
    # print the stats
    print(df.to_string())



