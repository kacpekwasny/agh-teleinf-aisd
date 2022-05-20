from sys import argv
from dataclasses import dataclass
from time import perf_counter

@dataclass
class Coords:
    x: int
    y: int

class Rotater:
    def __init__(self, matrix2D: list[list[int]]) -> None:
        self.matrix = matrix2D
        self.horizontal_ = True
        self.other_index = 0

    def horizontal(self): self.horizontal_ = True
    def vertical(self): self.horizontal_ = False
    def set_other_index(self, index: int): self.other_index = index

    def __getitem__(self, index: int):
        if self.horizontal_:
            return self.matrix[self.other_index][index]
        else:
            return self.matrix[index][self.other_index]


def file_translation(text: str, base=16) -> list[list[int]]:
    """
    convert text that contains chars of `base` to 2D matrix of integers
    """
    return [list(map(lambda x: int(x, base), line))
            for line in text.splitlines()
            if line.strip() != ""]


def find_hashes(lin: list[int], pattern: list[int], d: int, q: int) -> list[int]:
    """
    Return list of coordinates of where in the list does the patter match
    params:
        lin: list_in
        pattern: the pattern
        d: how many different values are there? ex.: if every item is a digit then d=10
        q: a prime number
    """
    lp = len(pattern)
    h = d ** (lp-1) % q
    coords = []

    # pattern hash
    phsh = 0
    for val in pattern:
        phsh = (d * phsh + val) % q

    hsh = 0
    for x in range(lp):
        hsh = (d * hsh + lin[x]) % q

    for x in range(len(lin) - lp):
        # if hashes match, then it is a high chance, that pattern matches too
        if hsh == phsh and pattern == lin[x:x+lp]:
            coords.append(x)

        # create a hash relying on previous hashes
        hsh = (d * (hsh - lin[x] * h) + lin[x + lp]) % q
        
    return coords


def find_karp(lines: list[list[int]], pattern: list[int], d: int, q: int) -> list[Coords]:
    cmh: list[Coords] = [] # coords matched horizontal
    for Y, line in enumerate(lines[:-len(pattern)]):
        coords_x = find_hashes(line, pattern, d, q)
        cmh += [ Coords(x, Y) for x in coords_x ]

    cmvh = [] # coords matched vertical and horizontaly
    for coords in cmh:
        to_check = []    
        match = False
        for y in range(len(pattern)):
            match = False
            if lines[coords.y + y][coords.x] != pattern[y]:
                break
            match = True
        if match:
            cmvh.append(coords)
    return cmvh


if __name__ == "__main__":
    file_path = argv[1]
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    start = perf_counter()
    matrix2d = file_translation(text)
    print(f"file translation: {perf_counter() - start = }")

    D = 16
    Q = 101

    pattern = [10, 11, 12]
    start = perf_counter()
    coords = find_karp(matrix2d, pattern, D, Q)
    print(f"find_karp: {perf_counter() - start = }")

    print(f"{len(coords) = }")
