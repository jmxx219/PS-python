from itertools import combinations


def pick01(N, M, picked, result):
    if M == 0:
        result.append(picked.copy())
        return
    smallest = 0 if len(picked) == 0 else picked[len(picked) - 1] + 1
    for next in range(smallest, N):
        picked.append(next)
        pick01(N, M - 1, picked, result)
        picked.pop()


def pickMFromN01(N, M):
    result = []
    picked = []
    pick01(N, M, picked, result)
    print(result)


def pick02(N, M, i, picked, result):
    if M == i:
        result.append(picked.copy())
        return
    smallest = 0 if i == 0 else picked[i - 1] + 1
    for next in range(smallest, N):
        picked[i] = next
        pick02(N, M, i + 1, picked, result)


def pickMFromN02(N, M):
    result = []
    picked = [None] * M
    pick02(N, M, 0, picked, result)
    print(result)


def pick03(N, M, idx, i, picked, result):
    if idx == M:
        result.append(picked.copy())
        return
    if i >= N: return
    picked[idx] = i;
    pick03(N, M, idx + 1, i + 1, picked, result)
    pick03(N, M, idx, i + 1, picked, result)


def pickMFromN03(N, M):
    result = []
    picked = [None] * M
    pick03(N, M, 0, 0, picked, result)
    print(result)


pickMFromN01(5, 2)
pickMFromN02(5, 2)
pickMFromN03(5, 2)

c = combinations([0, 1, 2, 3, 4], 2)
print(list(c))
