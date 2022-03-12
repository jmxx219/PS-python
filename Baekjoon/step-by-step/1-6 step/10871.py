T, m = map(int, input().split())

list = list(map(int, input().split()))

for i in range(T):
    if(m > list[i]):
        print(list[i], end=' ')
