m, n = map(int, input().split())
list_n = [i for i in range(2, n + 1)]

for i in range(0, n - 1):
    if list_n[i] == 0:
        continue

    for j in range(i + list_n[i], n - 1, list_n[i]):
        list_n[j] = 0

if m == 1:
    m += 1
for i in range(m - 2, n - 1):
    if list_n[i] != 0:
        print(list_n[i])