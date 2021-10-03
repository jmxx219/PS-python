# 대마법사의 크리스마스 선물
from sys import stdin


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def solve():
    _gcd = nums[0]

    for n in nums:
        _gcd = gcd(_gcd, n)

    return _gcd == 1

    return False


T = int(stdin.readline())
for _ in range(T):
    A = int(stdin.readline())
    nums = list(map(int, stdin.readline().split()))

    if solve(): print("true")
    else: print("false")