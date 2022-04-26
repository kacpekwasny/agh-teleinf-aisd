from collections import deque
from itertools import islice

def mergesort_deque(A: deque[int]) -> list[int]:
    mid = len(A) // 2
    if len(A)>1: A = merge_deque(mergesort_deque(deque(islice(A, 0, mid))), mergesort_deque(deque(islice(A, mid, len(A)))))
    return A

def merge_deque(l1: deque[int], l2: deque[int]) -> list[int]:
    ret = deque()
    while len(l1) and len(l2):
        if l1[0] < l2[0]: ret.append(l1.popleft())
        elif l1[0] > l2[0]: ret.append(l2.popleft())
        else: ret.extend([l1.popleft(), l2.popleft()])
    return ret + l1 + l2

def mergesort_list(A: list[int]) -> list[int]:
    mid = len(A) // 2
    if len(A)>1: A = merge_list(mergesort_list(A[:mid]), mergesort_list(A[mid:]))
    return A

def merge_list(l1: list[int], l2: list[int]) -> list[int]:
    ret = []
    while len(l1) and len(l2):
        if l1[0] < l2[0]: ret.append(l1.pop(0))
        elif l1[0] > l2[0]: ret.append(l2.pop(0))
        else: ret += [l1.pop(0), l2.pop(0)]
    return ret + l1 + l2

if __name__ == "__main__":
    print(f"{merge_list([1,4,5,6,10], [0,2,3,6,9,11]) = }")
    A = [1,7,3,1,56,2,3,3,5,74,223,56]
    print(f"{A = }")
    print(f"{mergesort_list(A) = }")

    print(f"{merge_deque(deque([1,4,5,6,10]), deque([0,2,3,6,9,11])) = }")
    A = deque([1,7,3,1,56,2,3,3,5,74,223,56])
    print(f"{A = }")
    print(f"{mergesort_deque(A) = }")
