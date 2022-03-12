a, b, c = map(int, input().split())
if c - b > 0:
    print(a // (c-b) + 1)
else:
    print(-1)
