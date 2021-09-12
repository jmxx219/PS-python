from collections import deque
from sys import stdin


def Bfs(visited, graph):
    # crash -  0: 벽안부시고 가는경우, 1: 부신 경우
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0][0] = 1

    while queue:
        cur_x, cur_y, isCrash = queue.popleft()
        if cur_x == row - 1 and cur_y == col - 1:
            return visited[cur_x][cur_y][isCrash]
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if next_x <= -1 or next_x >= row or next_y <= -1 or next_y >= col:
                continue

            # 벽 안부수고 이동
            if graph[next_x][next_y] == 0 and visited[next_x][next_y][isCrash] == 0:
                queue.append((next_x, next_y, isCrash))
                visited[next_x][next_y][isCrash] = visited[cur_x][cur_y][isCrash] + 1
            # 벽 부수고 이동
            if graph[next_x][next_y] == 1 and isCrash == 0:
                queue.append((next_x, next_y, isCrash + 1))
                visited[next_x][next_y][isCrash + 1] = visited[cur_x][cur_y][isCrash] + 1

    return -1


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
row, col = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().strip())) for _ in range(row)]
visited = [[[0] * 2 for _ in range(col)] for _ in range(row)]
print(Bfs(visited, graph))