import time
import concurrent.futures

start = time.perf_counter()

def do_something(secs):
    print(f"sleeping {secs} second(s)...")
    time.sleep(secs)
    return "Done sleeping.."


with concurrent.futures.ProcessPoolExecutor() as executor:
    f1 = executor.submit(do_something, 1)
    f2 = executor.submit(do_something, 1)
    print(f1.result())
    print(f2.result())

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
