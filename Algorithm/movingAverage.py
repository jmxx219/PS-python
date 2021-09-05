# O(n^2)
def movingAverage01(N, M):
    ret = [];
    for i in range(M - 1, len(N)):
        sum = 0
        for j in range(M):
            sum += N[i - j]
        ret.append(sum / M)
    return ret


# O(n)
def movingAverage02(N, M):
    ret = []
    sum = 0
    for i in range(M - 1):
        sum += N[i]
    for i in range(M - 1, len(N)):
        sum += N[i]
        ret.append(sum / M)
        sum -= N[i - M + 1]
    return ret


N = [1, 5, 4, 3, 2]
ret = movingAverage01(N, 2)
print(ret)
N = [1, 5, 4, 3, 2]
ret = movingAverage02(N, 2)
print(ret)
