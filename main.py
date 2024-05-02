from time import perf_counter
from threading import Thread
from multiprocessing import Process

from utils.num_functions import perfect_finder
from utils.list_utils import splitter

numbers = [i for i in range(2, 200_000)]

# Measuring execution time of cpu intensive task made sequentialy:
print("#----- Sequential -----#")
t = perf_counter()
perfect_finder(numbers)
t = perf_counter()-t
print(f"time elapsed: {t:.4f}s")
print()
print()

# splitting workload
numbers = splitter(numbers, 7)

# preparing threads
threads = [Thread(target=perfect_finder, args=[i]) for i in numbers]

print("#--- Multithreading ---#")
t = perf_counter()
for thread in threads:
	thread.start()
for thread in threads:
	thread.join()
t = perf_counter() - t
print(f"time elapsed: {t:.4f}s")
print()
print()

# preparing processes
processes = [Process(target=perfect_finder, args=[i]) for i in numbers]

print("#-- Multiprocessing ---#")
t = perf_counter()
for process in processes:
	process.start()
for process in processes:
	process.join()
t = perf_counter() - t
print(f"time elapsed: {t:.4f}s")
print()
