# 공유기 설치 - 이분탐색
# 참고: https://assaeunji.github.io/python/2020-05-07-bj2110/

from sys import stdin


def solve():
    start = 1 # 좌표값의 최소값
    end = housePos[-1] - housePos[0] # 가장 높은 좌표와 낮은 좌표의 차이
    res = 0

    while start <= end:
        mid = (start + end) // 2
        old = housePos[0] # 배열에서 가장 낮은 좌표
        cnt = 1 # 거리를 mid로 뒀을 때, 공유기 설치가 가능한 집의 개수

        for i in range(1, len(housePos)):
            if housePos[i] >= old + mid:
                cnt += 1
                old = housePos[i]

        if cnt >= C:
            start = mid + 1
            res = mid
        else:
            end = mid - 1

    return res


N, C = map(int, stdin.readline().split())
housePos = []
for i in range(N):
    housePos.append(int(stdin.readline()))
housePos.sort()
print(solve())
