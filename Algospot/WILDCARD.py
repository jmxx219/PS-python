from typing import List


def solve(files: List[str]) -> bool:
    pass


c = int(input())
for _ in range(c):
    w = input()
    n = int(input())

    files = []
    for i in range(n):
        files.append(input())

    for file in solve(files):
        print(file)
