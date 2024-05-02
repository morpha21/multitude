from time import perf_counter
from threading import Thread

from utils.num_functions import is_perfect
from utils.list_utils import splitter

numbers = [i for i in range(2, 30000)]

# Measuring execution time of cpu intensive task made sequentialy:
t = perf_counter()
for i in numbers:
	if is_perfect(i):
		print(i)
t = perf_counter()-t
print()
print()
print(f"time elapsed: {t:.4f}s")


numbers = splitter(numbers, 7)



# Measuring execution time of cpu intensive task made in multithreading:
#t = perf_counter()



#t = perf_counter()-t
#print()
#print()
#print(f"time elapsed: {t:.4f}s")



