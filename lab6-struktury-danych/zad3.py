from random import uniform, choice
from time import perf_counter

from zad1i2 import Forest, Tree


def gen(n: int) -> float:
    for _ in range(n):
        yield round(uniform(0, 100), 2)

def g() -> float:
    return round(uniform(0, 100), 2)


def main():
    loops = 100
    for items_num in [25, 50, 100, 500, 1000]:
        items = list(gen(items_num))
        f = Forest().insert_multiple(*items)

        print(f"{items_num=}")
    
        # INSERT
        start = perf_counter()
        for _ in range(loops):
            f.ins(g())
        elapsed = perf_counter() - start
        print(f"Insert into forest {loops=} {elapsed=} {elapsed/loops=}")
            
        # SEARCH
        start = perf_counter()
        for _ in range(loops):
            f.search(choice(items))
        elapsed = perf_counter() - start
        print(f"Search in forest {loops=} {elapsed=} {elapsed/loops=}")


        items = [t.value for t in f.trees]

        # MINIMUM
        start = perf_counter()
        for _ in range(loops):
            f.minimum(choice(items))
        elapsed = perf_counter() - start
        print(f"Maximum in a tree in forest {loops=} {elapsed=} {elapsed/loops=}")

        # MAXIMUM
        start = perf_counter()
        for _ in range(loops):
            f.maximum(choice(items))
        elapsed = perf_counter() - start
        print(f"Minimum in a tree in forest {loops=} {elapsed=} {elapsed/loops=}")

        print("\n")

if __name__ == "__main__":
    main()




