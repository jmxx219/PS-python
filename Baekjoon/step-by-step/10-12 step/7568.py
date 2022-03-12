n = int(input())
persons = []
lanks = [1] * n
for _ in range(n):
    persons.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if persons[i][0] < persons[j][0] and persons[i][1] < persons[j][1]:
            lanks[i] += 1

for lank in lanks:
    print(lank, end=" ")