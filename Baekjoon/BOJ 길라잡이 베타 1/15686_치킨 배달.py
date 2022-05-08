# 0: 빈칸, 1: 집, 2: 치킨집
# 거리 = |r2-r1| + |c2- c1|
# 수익을 많이 낼 수 있는 치킨 집 개수는 최대 M개
import itertools
import math
from sys import stdin
from typing import List


def shortest_distance(chicken_comb: List[int], house_list: List[int]):
    res = math.inf

    for chicken in chicken_comb:
        shortest = 0

        for house in house_list:
            distance = math.inf
            for m in range(M):
                distance = min(distance, abs(house[0] - chicken[m][0]) + abs(house[1] - chicken[m][1]))
            shortest += distance

        res = min(res, shortest)

    return res


def solve():

    house = []
    chicken = []

    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                chicken.append([i, j])
            if board[i][j] == 1:
                house.append([i, j])

    # print("house: " + str(house))
    # print("chicken: " + str(chicken))

    ch_comb = list(itertools.combinations(chicken, M))
    # print("chicken_combinations: " + str(ch_comb))

    return shortest_distance(ch_comb, house)


N, M = map(int, stdin.readline().split()) # 도시, 치킨 집 최대 개수
board = []
for _ in range(N):
    board.append(list(map(int, stdin.readline().split())))
print(solve())