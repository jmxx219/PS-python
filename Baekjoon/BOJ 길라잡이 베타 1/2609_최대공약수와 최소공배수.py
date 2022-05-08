from sys import stdin


def gcd(a: int, b: int):
    if b == 0:
        return a
    return gcd(b, a % b)


a, b = map(int, stdin.readline().split())
x = gcd(a, b) # 최대 공약수
y = (a * b) // x # 최소 공배수
print(x)
print(y)