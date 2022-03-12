from sys import stdin

N = int(stdin.readline())
values = list(map(int, stdin.readline().split()))
values.sort()

lo, hi = 0, N - 1
absMin = abs(values[lo] + values[hi])

i, j = lo, hi
while lo < hi:
    tmp = values[lo] + values[hi]
    if abs(tmp) < absMin:
        i = lo
        j = hi
        absMin = abs(tmp)
    if absMin == 0:
        break
    if tmp > 0:
        hi -= 1
    else:
        lo += 1

print(values[i], values[j])
