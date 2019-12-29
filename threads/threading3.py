#THis program starts 10 threads and waits for them to complete.
#Accept arguments in the fuction.

import time
import threading

start = time.perf_counter()


threads = []

def do_something(secs):
    print(f"sleeping {secs} second...")
    time.sleep(secs)
    print("Done sleeping..")

for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
