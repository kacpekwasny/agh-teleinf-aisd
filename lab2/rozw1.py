from time import time

def timeit(reps, *funcs):
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


"""yield all numbers that are divisable by `divisable` and not divisable by `not_divisable` from between the range <low, high)
FASTER than alt"""
def zad1(low, high, divisable, not_divisable):
    # for simplicty number is divisable - means that it is divisable by `divisable` variable. Similarly not divisable.
    divisable, not_divisable = abs(divisable), abs(not_divisable)
    if divisable == not_divisable:
        return

    i = low
    i = i + divisable - (i % divisable) if i % divisable > 0 else i  # i is now first divisable number >= low
    delta = divisable * not_divisable # this number is divisable and not divisable
    till_next = delta - (i % delta)

    while i < high:
        if till_next > 0:
            yield i
        else:
            till_next = delta
        till_next -= divisable
        i += divisable

def zad1_alt(low, high, divisable, not_divisable):
    for i in range(low, high):
        if i % divisable == 0 and i % not_divisable != 0:
            yield i
def test_gen(gen, *args):
    def f():
        for _ in gen(*args):
            continue
    f.__name__ = gen.__name__
    return f

def turn2str(gen, *args):
    conv = ""
    prev2 = False
    for i in gen(*args):
        s = str(i).replace("21", "XX")
        if prev2 and s[0] == "1":
            conv = conv[:-1] + "XX" + s[1:]
        prev2 = s[-1] == "2"

"""FASTER than original"""
def turn2str_alt(gen, *args): # faster
    return "".join([str(i) for i in gen(*args)]).replace("21", "XX") 


if __name__ == "__main__":
    args = 500, 3000, 7, 5
    timeit(1000, test_gen(zad1, *args), test_gen(zad1_alt, *args))
    timeit(1000, lambda: turn2str(zad1, *args), lambda: turn2str_alt(zad1, *args))
    # [print(i, i%5, i%7) for i in zad1(500, 601, 5, 7)]

