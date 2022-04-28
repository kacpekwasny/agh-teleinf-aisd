import matplotlib.pyplot as plt


# https://github.com/kacpekwasny/agh-teleinf-aisd
import sys, os
sys.path.append(os.path.abspath(r".."))

from aidslib.time_measurements import exec_time

from zad1 import hanoi, gen_hanoi
from zad2 import Hanoi

def measure_time():
    rec = {}
    it = {}

    reps = 10
    for size in range(3, 20):
        # measure time for recursive algo
        avg, _ = exec_time(
            reps,
            lambda: hanoi(size, *gen_hanoi(size))
        )
        rec[size] = avg

        # measure time for recursive algo
        h = Hanoi()
        def solve():
            h.gen_tower(size)
            h.solve()

        avg, _ = exec_time(reps, solve)
        it[size] = avg

        print(size)
        print(rec)
        print(it)

    return rec, it

def plot(rec: dict[int | float], it: dict[int | float]):
    plt.plot(list(rec.keys()), list(rec.values()))
    plt.plot(list(it.keys()), list(it.values()))
    
    plt.xlabel('tower size')
    plt.ylabel('avg execution time in seconds')
    
    plt.title('dependence of the execution time on the size of the tower')
    
    plt.show()

if __name__ == "__main__":
    plot(*measure_time())
