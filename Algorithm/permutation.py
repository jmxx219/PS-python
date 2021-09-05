from itertools import permutations


def permutate(N, i, flag, curr):
    if i == N:
        print(curr)
        return
    for j in range(N):
        if not flag[j]:
            flag[j] = True
            curr[i] = j + 1
            permutate(N, i + 1, flag, curr)
            flag[j] = False


def permutation01(N):
    flag = [False] * N
    curr = [None] * N
    permutate(N, 0, flag, curr)


def permutation02(N):
    P = []
    P.append([1])
    for i in range(1, N):
        n = i + 1
        tmp = []
        for j in range(len(P)):
            curr = P.pop()
            for k in range(len(curr) + 1):
                next = curr.copy()
                next.insert(k, n)
                tmp.append(next)
        P = tmp
    print(P)


permutation01(3)
permutation02(3)

L = [1, 2, 3]
p = permutations(L, 3)
print(list(p))
