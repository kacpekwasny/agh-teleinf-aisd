from sys import argv
from time import perf_counter


def get_content_2D(file_path) -> list[str]:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    return [l for l in content.split("\n") if l.strip() != ""]

def find_occurrences(content: list[str]) -> tuple[int, int]:
    """
    generator yields coordinates of where in the 2D matrix the pattern can be found

    """
    for y, line in enumerate(content[:-2]):
        for x in range(len(line) - 2):
            if (line[x:x+3] == "ABC"
            and content[y+1][x]=="B" and content[y+2][x]=="C"):
                yield y, x

if __name__ == "__main__":
    lines = get_content_2D(argv[1])
    i = 0
    start = perf_counter()
    for y, x in find_occurrences(lines):
        i += 1
    print(f"{perf_counter() - start = }")
    print(i)



