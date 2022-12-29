import os

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

import os,ip address
os.system('cls')

while True:
    ip= input
    ('Enter IP address: ')
    try:
        print(ip address.ip_address(ip))
        print('IP Valid')
    except:
        print('-' *50)
        print('IP is not valid ')
    finally:
        if ip=='mango':
            print('Script Finished')
            break
