from time import perf_counter
from typing import Tuple, TypeVar
Any = TypeVar("Any")

def timeit(reps, *funcs):
    for f in funcs:        
        s = perf_counter()
        for _ in range(reps):
            f()
        print("\n", f.__name__)
        print((perf_counter()-s)/reps)
        print("\n")

def timeit_compare(reps, *funcs):
    if len(funcs) != 2: raise ValueError("you can only compare two functions at a time")
    times = []
    for f in funcs:        
        s = perf_counter()
        for _ in range(reps):
            f()
        print("\n", f.__name__)
        times.append( (perf_counter()-s) / reps )
        print(times[-1])
        print("\n")
    for i in range(len(times)-1):
        x = times[i]/times[i+1]
        print(x, 1/x)

def timeit_dict(reps, **funcs) -> dict:
    """
        returns:
            kwarg -> elapsed_time
    """
    exec_times = {}
    for name, func in funcs.items():
        print(f"Starting {name}: ")
        s = perf_counter()
        for rep in range(reps):
            func()
            print(f"{rep=} : {perf_counter() - s = }")
            #print(". ", end="", flush=True)
        exec_times[name] = perf_counter() - s
        print(f"\n {name} - execution of {reps=} took time: {exec_times[name]} \n")
    return exec_times

def time_exec_ret(func, *args, **kwargs) -> Tuple[Any, float]:
    start = perf_counter()
    ret = func(*args, **kwargs)
    return ret, perf_counter() - start

def exec_time(reps, func) -> float:
    "returns avg_time, full_time"
    start = perf_counter()
    for _ in range(reps):
        func()
    elapsed = perf_counter() - start
    return elapsed/reps, elapsed

