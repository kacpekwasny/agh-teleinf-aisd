import sys, os
from unicodedata import name
sys.path.append(os.path.abspath(r".."))

from random import randint

from aidslib.time_measurements import timeit_dict
from zad1 import insertion
from zad2 import mergesort



def main():
    items100 = lambda: [randint(0, 1000) for _ in range(10**2)]
    items1k = lambda: [randint(0, 1000) for _ in range(10**3)]
    items10k = lambda: [randint(0, 1000) for _ in range(10**4)]
    items50k = lambda: [randint(0, 1000) for _ in range(5*10**4)]

    measurements = timeit_dict(
        10,
        insert_100_items = lambda: insertion(items100()),
        insert_1k_items = lambda: insertion(items1k()),
        insert_10k_items = lambda: insertion(items10k()),
        insert_100k_items = lambda: insertion(items50k()),
    )

    for k, v in measurements.items():
        print(f"{k} reps=10 elapsed in {v} seconds. Avg={v/10}")

    measurements = timeit_dict(
        100,
        mergesort_100_items = lambda: mergesort(items100()),
        mergesort_1k_items = lambda: mergesort(items1k()),
        mergesort_10k_items = lambda: mergesort(items10k()),
        mergesort_100k_items = lambda: mergesort(items50k()),
    )

    for k, v in measurements.items():
        print(f"{k} reps=10 elapsed in {v} seconds. Avg={v/10}")


if __name__ == "__main__":
    main()
