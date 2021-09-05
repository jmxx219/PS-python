from sys import stdin


def allSame(y: int, x: int, n: int):
    for i in range(y, y + n):
        for j in range(x, x + n):
            if paper[y][x] != paper[i][j]:
                return False
    return True


def solve(y: int, x: int, n: int):
    if allSame(y, x, n):
        colors[paper[y][x]] += 1
        return
    solve(y, x , n // 2) # 왼쪽 위
    solve(y, x + n // 2, n // 2) # 오른쪽 위
    solve(y + n // 2, x, n // 2) # 왼쪽 아래
    solve(y + n // 2, x + n // 2, n // 2) # 오른쪽 아래


N = int(input())
paper = []
colors = [0, 0] # 하얀색, 파랑색
for _ in range(N):
    paper.append(list(map(int, stdin.readline().split())))

solve(0, 0, N)

print(colors[0])
print(colors[1])