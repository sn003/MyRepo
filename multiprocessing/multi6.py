import time
import concurrent.futures

start = time.perf_counter()

def do_something(secs):
    print(f"sleeping {secs} second(s)...")
    time.sleep(secs)
    return f"Done sleeping..{secs}"


secs = [5, 4, 3, 2, 1]
with concurrent.futures.ProcessPoolExecutor() as executor:
    results = [executor.submit(do_something, sec) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
