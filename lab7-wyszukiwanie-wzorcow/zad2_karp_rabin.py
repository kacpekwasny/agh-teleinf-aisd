from time import perf_counter


def hash_2d(in2d: list[list[int]], pattern: list[int]) -> list[list[int]]:
    """
    Create a 2D matrix that contains hashes of vetical occurances.
    
    """
    lp = len(pattern)
    lx = len(in2d[0])   # length of every line
    ly = len(in2d)      # vertical height

    hash_table = []

    for y, line in enumerate(in2d):
        for x in range(lx - lp):
            # create a hash relying on previous hashes (if they exist)
            if x > lp - 1:
                hash_table.append()



    pass














