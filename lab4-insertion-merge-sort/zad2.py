def mergesort(A: list[int]) -> list[int]:
    if len(A)>1:
        A = merge(mergesort(A[:len(A) // 2]), mergesort(A[len(A) // 2:]))
    return A

def merge(l1: list[int], l2: list[int]) -> list[int]:
    ret = []
    while len(l1) and len(l2):
        if l1[0] < l2[0]: ret.append(l1.pop(0))
        elif l1[0] > l2[0]: ret.append(l2.pop(0))
        else: ret += [l1.pop(0), l2.pop(0)]
    return ret + l1 + l2

if __name__ == "__main__":
    print(f"{merge([1,4,5,6,10], [0,2,3,6,9,11]) = }")
    A = [1,7,3,1,56,2,3,3,5,74,223,56]
    print(f"{A = }")
    print(f"{mergesort(A) = }")

