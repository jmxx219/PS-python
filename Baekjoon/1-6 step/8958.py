n = int(input())
for i in range(n):
    result = 0
    quiz = list(str(input()))
    sum = 0
    for j in range(len(quiz)):
        if quiz[j] == 'X':
            sum = 0
        else:
            sum += 1
            result += sum
    print(result)