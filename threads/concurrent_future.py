
import time
import concurrent.futures

start = time.perf_counter()

def do_something(secs):
    print(f"sleeping {secs} second...")
    time.sleep(secs)
    return f"Done sleeping..{secs}"

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [3, 5, 4, 1, 2]
    results = [ executor.submit(do_something, sec) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
