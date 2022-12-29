import concurrent.futures
import time
start =time.perf_counter()
def calculateTime(seconds):
    print(f"sleep for{seconds} second \n")
    time.sleep(seconds)
    return (f"completed{seconds} sleep \n")

with concurrent.futures.ThreadPoolExecutor() as executor:
    results=[executor.submit(calculateTime,2) for _ in range(5)]

    #for _ in range(5):
        #thread = threading.Thread(target=calculateTime,args=[3])
        #thread.start()
        #threads.append(thread)

    for r in concurrent.futures.as_completed(results):
        print(r)
        print(r.result())

finish= time.perf_counter()

