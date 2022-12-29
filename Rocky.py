"""import os

with open("ip_list.txt") as file:
    park= file.read()
    park = park.splitlines()
    print("(park) \n")
    # ping for each ip in the file
for ip in park:

    response=os.popen(f"ping(ip)").read()
    # savingf some ping output details to output file
    if ("Request timed out." or "unreachable") in response:
        print(response)
        f= open(" info output .txt","a")
        f.write(str(ip) + 'link is down '+'\n')
        f.close()
    else:
        print(response)
        f = open(" info output .txt", "a")
        f.write(str(ip) + 'is up ' + '\n')
        f.close()

with open(" info_output .txt",) as file:
    output=file.read()
    print(output)
with open("info.output.txt","w"):
    pass
"""
import os, ipaddress
os.system('cls')

while True:
    ip= input('Enter IP adress: ')
    try:
        print(ipaddress.ip_address(ip))
        print('IP Valid')
    except:
        print('-' *50)
        print('IP is not valid ')
    finally:
        if ip=='mango':
            print('Script Finished')
            break

import os
print(os.system("ipconfig"))

import socket
s=socket.socket()
port=40674
s.connect(('127.0.0.1',port))



'''from netmiko import ConnectHolder
CSR={
    "device_type": "cisco_ios",
    "ip":"sandbox-iosxe-latest-1.cisco.com",
    "username":"developer",
    "password":"C1sco12345"
}
net_connect = ConnectHandler(**CSR)
output=net_connect.send_command('show ip int brief')
print (output)'''


