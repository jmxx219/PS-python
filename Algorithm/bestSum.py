from sys import stdin


def solve_memo(m, nums, memo):
    if m < 0: return None
    if m == 0: return []
    if m in memo: return memo.get(m)
    best = None
    for x in nums:
        if m - x < 0: continue
        curr = solve_memo(m - x, nums, memo)
        if curr is not None and (best is None or len(best) > len(curr) + 1):
            best = curr[:]
            best.append(x)
    memo[m] = best
    return best


def solve_dp(m, nums):
    table = [None for _ in range(m + 1)]
    table[0] = []
    for i in range(m):
        if table[i] is not None:
            for x in nums:
                if i + x <= m:
                    if table[i + x] is None or len(table[i + x]) > len(table[i]) + 1:
                        table[i + x] = table[i][:]
                        table[i + x].append(x)
    return table[m]


def main_memo():
    T = int(stdin.readline())
    for _ in range(T):
        M, N = list(map(int, stdin.readline().split()))
        nums = list(map(int, stdin.readline().split()))
        memo = dict()
        best = solve_memo(M, nums, memo)
        if best is not None:
            print(len(best), ' '.join(str(i) for i in best))
        else:
            print(-1)


def main_dp():
    T = int(stdin.readline())
    for _ in range(T):
        M, N = list(map(int, stdin.readline().split()))
        nums = list(map(int, stdin.readline().split()))
        best = main_dp(M, nums)
        if best is not None:
            print(len(best), ' '.join(str(i) for i in best))
        else:
            print(-1)

main_memo()
main_dp()