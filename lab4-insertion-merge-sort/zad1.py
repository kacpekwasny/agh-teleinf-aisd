from random import randint
from sys import argv


def insertion(A: list[int]) -> list[int]:
    A = A[:]
    for i in range(1, len(A)):
        x = A[i]
        j = i - 1
        while j >= 0 and A[j] > x:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = x
    return A


if __name__ == "__main__":
    limit = 30
    A = [randint(0, 1000) for i in range(int(argv[1]))]
    print()
    print(f"{A[:limit] = }{'...' if len(A)>30 else ''}")
    print(f"{insertion(A)[:limit] = }{'...' if len(A)>30 else ''}")
    print()


