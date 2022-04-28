def gen_hanoi(tower_height: int) -> list[list[int]]:
    """
    returns:
        [
            [tower_height ... 2, 1],
            [],
            []
        ]
    """
    if tower_height < 1: raise ValueError("tower_height argument has to be at least 1")
    return [list(range(1, tower_height+1))[::-1], [], []]


def hanoi(n, sour: list[int], dest: list[int], buff: list[int]):
    #print(n, sour, dest, buff)
    if n==1:
        dest.append(sour.pop())
        return
    hanoi(n-1, sour, buff, dest)
    dest.append(sour.pop())
    hanoi(n-1, buff, dest, sour)


if __name__ == "__main__":
    num = 6
    h = gen_hanoi(num)
    hanoi(num, *h)
    print(h)
