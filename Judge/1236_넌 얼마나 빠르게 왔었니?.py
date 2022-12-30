import collections
from sys import stdin


def solve():
    students = collections.defaultdict(list)

    for i in range(N):
        students[number[i]].append(i + 1)

    for n in qNumber:
        if n in students:
            for x in students[n]:
                print(x, end=" ")
            print()
        else:
            print(-1)


N = int(stdin.readline())  # 상담한 학생 수
number = list(map(int, stdin.readline().split()))  # 학번
Q = int(stdin.readline())  # 순서를 알고싶은 학생 수
qNumber = list(map(int, stdin.readline().split()))  # 학번
solve()