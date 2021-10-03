def computeLPSArray(pat, M, lps):
    length = 0

    # 항상 lps[0]==0 이므로 while문은 i==1부터 시작한다.
    i = 1
    while i < M:
        if pat[i] == pat[length]: # 이전 인덱스에서 같았다면 다음 인덱스만 비교하면 된다.
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1


def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)

    lps = [0] * M
    computeLPSArray(pat, M, lps)

    j = 0 # index for txt[]
    i = 0 # index for pat[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            print("Found pattern at index " + str(i - j))
            j = lps[j - 1]

        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


pat = "ABABCABAB"
txt = "ABABDABACDABABCABAB"
KMPSearch(pat, txt)