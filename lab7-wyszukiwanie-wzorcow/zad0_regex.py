from sys import argv
from time import perf_counter
import regex as re

# WRONG SOLUTION
# beacuse of the removed newlines


def get_content(file_path) -> tuple[str, int]:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    # find line length
    for i, l in enumerate(content):
        if l == "\n": 
            return content, i

def find(content, regex_str) -> list[tuple[int, int]]:
    coords: list[tuple[int, int]] = []
    pattern = re.compile(regex_str)
    for match in pattern.finditer(content):
        yield match.start()

if __name__ == "__main__":
    # This is actually a wrong solution

    content, line_len = get_content(argv[1])
    start_perf = perf_counter()
    restr = f"ABC.{'{'}{line_len-3}{'}'}B.{'{'}{line_len-1}{'}'}C"
    count = 0
    for start in find(content.replace("\n", ""), restr):
        count += 1
        if False:
            print(start//line_len, start%line_len)
            print(content[start:start+3])
            print(content[start + line_len])
            print(content[start + line_len * 2])
    print(f"{count = }")
    print(f"{perf_counter() - start_perf = }")

