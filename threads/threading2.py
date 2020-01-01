#THis program starts 10 threads and waits for them to complete.

import time
import threading

start = time.perf_counter()


threads = []

def do_something():
    print("sleeping 1 second...")
    time.sleep(1)
    print("Done sleeping..")

for _ in range(10):
    t = threading.Thread(target=do_something)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
