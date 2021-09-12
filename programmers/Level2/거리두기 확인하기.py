dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]


def isRange(y, x):
    return 0 <= x < 5 and 0 <= y < 5


def direction2(y, x,  place): # 2중 for문: 4방향씩 탐색하면서, P가 탐색되면 False를 리턴한다.
    for i in range(4):
        newY1 = y + dy[i]
        newX1 = x + dx[i]
        if isRange(newY1, newX1):
            if place[newY1][newX1] == "X":
                continue
            if place[newY1][newX1] == "P":
                return False
            for j in range(4):
                newY2 = newY1 + dy[j]
                newX2 = newX1 + dx[j]
                if isRange(newY2, newX2) and not (y == newY2 and x == newX2):
                    if place[newY2][newX2] == "X":
                        continue
                    if place[newY2][newX2] == "P":
                        return False
    return True


def direction(Y, X, y, x, place, depth): # 재귀: 4방향씩 탐색하면서, P가 탐색되면 False를 리턴한다.
    if depth > 2:
        return True
    for i in range(4):
        newY1 = y + dy[i]
        newX1 = x + dx[i]
        if isRange(newY1, newX1) and not (newY1 == Y and newX1 == X):
            if place[newY1][newX1] == "X":
                continue
            if place[newY1][newX1] == "P":
                return False
            if not direction(Y, X, newY1, newX1, place, depth + 1):
                return False
    return True


def solve(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P" and not direction(i, j, i, j, place, 1):
                return 0

    return 1


def solution(places):
    res = [0, 0, 0, 0, 0]

    for i in range(5):
        res[i] = solve(places[i])

    return res


places = [
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
]

print(solution(places))