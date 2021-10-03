from sys import stdin


def find(parent, i):
    if parent[i] == i:
        return i
    parent[i] = find(parent, parent[i])
    return parent[i]


def union(parent, childSize, uP, vP):
    p = uP
    c = vP

    if childSize[uP] < childSize[vP]:
        p = vP
        c = uP
    parent[c] = p
    childSize[p] += childSize[c]
    childSize[c] = 0


def mst():
    parent = []
    childSize = []

    for node in range(N):
        parent.append(node)
        childSize.append(1)

    # result = []
    result  = 0
    i = e = 0
    while e < N - 1:
        u, v, w = graph[i]
        uP = find(parent, u)
        vP = find(parent, v)

        if uP != vP:
            e = e + 1
            result += w
            # result.append([u, v, w])
            union(parent, childSize, uP, vP)
        i = i + 1

    return result


T = int(stdin.readline())
for _ in range(T):
    N, E = map(int, stdin.readline().split())
    graph = []
    tmp = list(map(int, stdin.readline().split()))
    for i in range(0, len(tmp), 3):
        graph.append([tmp[i], tmp[i+1], tmp[i+2]])
    graph = sorted(graph, key=lambda item: item[2])
    print(mst())
