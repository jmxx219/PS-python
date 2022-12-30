from collections import Counter
from sys import stdin


def solve():
    words_cnt = Counter(sts)
    for word in words_cnt.keys():
        if words_cnt[word] % N != 0:
            print('false')
            return
    print('true')


N = int(stdin.readline())
sts = ''
for _ in range(N):
    sts += stdin.readline().rstrip()
solve()