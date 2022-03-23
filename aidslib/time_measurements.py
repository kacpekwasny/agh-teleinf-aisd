from time import time
from typing import Tuple, TypeVar
Any = TypeVar("Any")

def timeit(reps, *funcs):
    for f in funcs:        
        s = time()
        for _ in range(reps):
            f()
        print("\n", f.__name__)
        print((time()-s)/reps)
        print("\n")

def timeit_compare(reps, *funcs):
    if len(funcs) != 2: raise ValueError("you can only compare two functions at a time")
    times = []
    for f in funcs:        
        s = time()
        for _ in range(reps):
            f()
        print("\n", f.__name__)
        times.append( (time()-s) / reps )
        print(times[-1])
        print("\n")
    for i in range(len(times)-1):
        x = times[i]/times[i+1]
        print(x, 1/x)

def timeit_dict(reps, **funcs) -> dict:
    exec_times = {}
    for name, func in funcs.items():
        s = time()
        for _ in range(reps):
            func()
        exec_times[name] = time() - s
        print(f"\n {name} exec time: {exec_times[name]} \n")
    return exec_times

def time_exec_ret(func, *args, **kwargs) -> Tuple[Any, float]:
    start = time()
    ret = func(*args, **kwargs)
    return ret, time() - start

