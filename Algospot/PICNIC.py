from sys import stdin


def countFairings():
    firstIndex = -1

    for i in range(N):
        if not match[i]:
            firstIndex = i
            break

    if firstIndex == -1:
        return 1

    count = 0
    for i in range(firstIndex, N):
        if not match[i] and isFriends[firstIndex][i]:
            match[i] = match[firstIndex] = True
            count += countFairings()
            match[i] = match[firstIndex] = False

    return count


t = int(stdin.readline())
for _ in range(t):
    N, friends_n = map(int, stdin.readline().split())
    isFriends = [[False] * N for _ in range(N)]
    pair = list(map(int, stdin.readline().split()))
    match = [False] * N

    for i in range(0, len(pair), 2):
        isFriends[pair[i]][pair[i + 1]] = isFriends[pair[i + 1]][pair[i]] = True
    print(countFairings())