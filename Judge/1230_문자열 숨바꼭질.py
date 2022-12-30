from sys import stdin


def computeLPS(M, lps):
    length = 0
    i = 1
    while i < M:
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1


def Kmp():
    M = len(pat)
    N = len(txt)

    lps = [0] * M
    computeLPS(M, lps)

    j = 0  # pat
    i = 0  # txt

    res = []
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == M:
            res.append((i - j + 1))
            j = lps[j - 1]

        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    if len(res) == 0:
        print(0)
    else:
        print(len(res))
        for i in res:
            print(i, end=" ")
        print()


T = int(stdin.readline())
for _ in range(T):
    txt, pat = map(str, stdin.readline().strip().split())
    Kmp()