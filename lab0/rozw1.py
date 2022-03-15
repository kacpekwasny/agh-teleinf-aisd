from msilib.schema import Error
from time import time
from tokenize import Name

def timeit(reps, *funcs):
    for f in funcs:        
        s = time()
        for _ in range(reps):
            f()
        print("\n", f)
        print((time()-s)/reps)
        print("\n")

def z1():
    l = [1, 2]
    for _ in range(48-2):
        a, b = l[-1], l[-2]

        l.append((a+b)//(a-b))
    
    #print("avg: ", sum(l)/len(l))
    sr = sorted(l)
    #print("median: ", sum(sr[23:25])/2)
    
    d = {}
    for i in sr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    #for k, v in d.items():
    #    print(f"{k} has occured {v} times")        


from array import array
def z2():
    l = array("b", [1, 2])
    for _ in range(48-2):
        a, b = l[-1], l[-2]

        l.append((a+b)//(a-b))
    
    #print("avg: ", sum(l)/len(l))
    sr = sorted(l)
    #print("median: ", sum(sr[23:25])/2)
    
    d = {}
    for i in sr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    #for k, v in d.items():
    #    print(f"{k} has occured {v} times")        


timeit(100, z1, z2)

def z3():
    def z1():
        j = 0
        for i in "string":
            #print(i, end=" ")
            j += 1
        #print("\n")

    def z2():
        i = 0
        while i<12:
            #print(i, end=" ")
            i+=1
        #print("\n")

    timeit(100, z1, z2)

z3()


def z4():
    try:
        raise IndexError("index doesnt exist")
    except IndexError:
        try:
            raise ZeroDivisionError("remember you cholera do not divide by zero")
        except ZeroDivisionError:
            try:
                raise NameError("my name should be different")
            except NameError:
                print("name error cought")
z4()