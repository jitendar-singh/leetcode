import time
import concurrent.futures
start_time = time.perf_counter()
def dosomething():
    time.sleep(1)

threads = []

for _ in range(10):
    with concurrent.futures.ThreadPoolExecutor as executor:
        executor.submit(dosomething)
        threads.append(t1)

for thread in threads:
    thread.join()

finish_time = time.perf_counter()
print("Time taken:",round(finish_time - start_time,2))
