T = int(input())
for _ in range(T):
    k = int(input()) # 층
    n = int(input()) # 호
    people = [i for i in range(1, n + 1)]
    for __ in range(k):
        for j in range(1, n):
            people[j] += people[j - 1]
    print(people[-1])