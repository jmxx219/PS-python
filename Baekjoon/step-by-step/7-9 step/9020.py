def prime_list(n):
    prime_n = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if prime_n[i]:
            for j in range(i + i, n, i):
                prime_n[j] = False
    return [i for i in range(2, n) if prime_n[i]]


def sol(n):
    li = prime_list(n)
    print(li)
    idx = max([i for i in range(len(li)) if li[i] <= n / 2])
    for i in range(idx, -1, -1):
        for j in range(i, len(li)):
            print(f'{i}, {j}')
            if li[i] + li[j] == n:
                return li[i], li[j]


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        x, y = sol(n)
        print(x, y)
