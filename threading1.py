'''import time
import threading

start = time.perf_counter()

def calculateTime():
    print("sleep for 10 second \n")
    time.sleep(10)
    print("complete sleep \n")
t1= threading.Thread(target=calculateTime)
t2= threading.Thread(target=calculateTime)
t3= threading.Thread(target=calculateTime)
t4= threading.Thread(target=calculateTime)

t1.start()
t2.start()
t3.start()
t4.start()


t1.join()
t2.join()
t3.join()
t4.join()

finish=time.perf_counter()
print(finish-start,'seconds')'''


import time
import threading

start = time.perf_counter()

def calculateTime():
    print("sleep for 10 second \n")
    time.sleep(10)
    print("complete sleep \n")
threads=[]

for _ in range(5):
    thread=threading.Thread(target=calculateTime)
    thread.start()
    threads.append(thread)

for i in threads:
    i.join()

finish= time.perf_counter()
print(finish-start,"seconds")