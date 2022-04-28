import sys, os
sys.path.append(os.path.abspath(r".."))

from random import randint
from collections import deque

from aidslib.time_measurements import timeit_dict
from zad1 import insertion
from zad2 import mergesort_list, mergesort_deque



def main():
    items100 = lambda: [randint(0, 1000) for _ in range(10**2)]
    items1k = lambda: [randint(0, 1000) for _ in range(10**3)]
    items10k = lambda: [randint(0, 1000) for _ in range(10**4)]
    items50k = lambda: [randint(0, 1000) for _ in range(5*10**4)]

    reps = 0
    measurements = timeit_dict(
        reps,
        insert_100_items = lambda: insertion(items100()),
        insert_1k_items = lambda: insertion(items1k()),
        insert_10k_items = lambda: insertion(items10k()),
        insert_100k_items = lambda: insertion(items50k()),
    )

    reps = 1 if not reps else reps
    for k, v in measurements.items():
        print(f"{k} reps=10 elapsed in {v} seconds. Avg={v/reps}")

    reps = 100
    measurements = timeit_dict(
        reps,
#        mergesort_100_items = lambda: mergesort_list(items100()),
 #       mergesort_1k_items = lambda: mergesort_list(items1k()),
  #      mergesort_10k_items = lambda: mergesort_list(items10k()),
        mergesort_50k_items = lambda: mergesort_list(items50k()),
    )

    for k, v in measurements.items():
        print(f"{k} reps=10 elapsed in {v} seconds. Avg={v/reps}")

    reps = 100
    measurements = timeit_dict(
        reps,
#        mergesort_100_items = lambda: mergesort_deque(deque(items100())),
 #       mergesort_1k_items = lambda: mergesort_deque(deque(items1k())),
  #      mergesort_10k_items = lambda: mergesort_deque(deque(items10k())),
        mergesort_50k_items = lambda: mergesort_deque(deque(items50k())),
    )

    for k, v in measurements.items():
        print(f"{k} reps=10 elapsed in {v} seconds. Avg={v/reps}")




if __name__ == "__main__":
    main()
