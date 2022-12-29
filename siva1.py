
import uuid
print("The MAC adress in formatted way is :", end="")
print(':'.join(['{:02x}' . format ((uuid.getnode() >> ele)& 0xff)
for ele in range(0,8*6,8)][::-1]))  #8*6 is 8bits and 6parts with range 00 to ff

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(s)