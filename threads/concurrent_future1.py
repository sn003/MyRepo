
import time
import concurrent.futures

start = time.perf_counter()

def do_something(secs):
    print(f"sleeping {secs} second...")
    time.sleep(secs)
    return f"Done sleeping..{secs}"

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [ 5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
