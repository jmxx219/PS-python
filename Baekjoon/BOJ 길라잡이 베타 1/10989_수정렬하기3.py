# 수 정렬하기 3 - 카운팅 정렬
# 참고: https://bowbowbow.tistory.com/8
# 공간복잡도 O(n+k)

import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)