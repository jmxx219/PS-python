# 1213121
from sys import stdin


def check(num_size: int):
    for i in range(1, num_size // 2 + 1):
        if target[-i:] == target[-2*i : -i]:
            return False

    return True


def solve(num_len: int):

    if not check(num_len + 1):
        return False
    elif num_len == N:
        return True

    for i in range(1, 4):
        target.append(str(i))
        if solve(num_len + 1):
            return True
        target.pop()


N = int(stdin.readline())
target = []
solve(0)
print(''.join(target))