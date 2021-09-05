from sys import stdin

def solve(n: int):
    if n == 1:
        return a % c
    tmp = solve(n // 2)
    if n % 2 == 1:
        return a * tmp * tmp % c
    return tmp * tmp % c

a, b, c = map(int, stdin.readline().split())
print(solve(b))