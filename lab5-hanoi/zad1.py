from multiprocessing.sharedctypes import Value


def gen_hanoi(tower_height: int) -> list[list[int]]:
    """
    returns:
        [
            [1, 2, ... tower_height],
            [],
            []
        ]
    """
    if tower_height < 1: raise ValueError("tower_height argument has to be at least 1")
    return [list(range(1, int+1)).reverse(), [], []]


def solve_hanoi(hanoi: list[list[int]]) -> list[list[int]]:
    """
    yield next steps of the process of rebuilding the hanoi tower
    """
    
