import time
import concurrent.futures

start = time.perf_counter()

def do_something(secs):
    print(f"sleeping {secs} second(s)...")
    time.sleep(secs)
    return f"Done sleeping..{secs}"


secs = [5, 4, 3, 2, 1]
with concurrent.futures.ProcessPoolExecutor() as executor:
    results = executor.map(do_something, secs)

    for result in results:
        print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
