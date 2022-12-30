from typing import List

graph = { # 인접리스트로 구현한 그래프
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

# pop : 방문
# discovered : 발견
def recursive_dfs(v, discovered=[]) -> List[int]:
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            recursive_dfs(w, discovered)
    return discovered

# 발견 후 바로 방문, 발견 방문 시점 같음
def iterative_dfs(start_v) -> List[int]:
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered


# 방문 != 발견, 모두 발견한 후 방문
def iterative_bfs(start_v) -> List[int]:
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered


print(recursive_dfs(1))
print(iterative_dfs(1))
print(iterative_bfs(1))