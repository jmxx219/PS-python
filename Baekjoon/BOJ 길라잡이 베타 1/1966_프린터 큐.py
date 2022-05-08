from collections import defaultdict
from sys import stdin


def solve():
    index = [i for i in range(N)]
    index[M] = 'target'  # 내가 찾고 싶은 index
    cnt = 0

    while priority:
        if priority[0] == max(priority):
            cnt += 1
            if index[0] == 'target':
                break
            priority.pop(0)
            index.pop(0)
        else:
            priority.append(priority.pop(0))
            index.append(index.pop(0))

    return cnt


if __name__ == "__main__":
    T = int(stdin.readline())

    for i in range(T):
        N, M = map(int, stdin.readline().split())  # 문서 개수, 궁금한 문서
        priority = list(map(int, stdin.readline().split()))

        print(solve())
