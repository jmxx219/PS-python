# 이진 검색 트리
import sys
sys.setrecursionlimit(10**6)

preorder = []


def partition(root, start, end):
    for i in range(start, end+1):
        if preorder[root] < preorder[i]:
            return i - 1
    return root


def postorder(start, end):
    if start > end : return

    mid = partition(start, start+1, end)

    postorder(start+1, mid)
    postorder(mid+1, end)

    root = preorder[start]
    print(root)


while True:
    try:
        preorder.append(int(input()))
    except:
        break

postorder(0, len(preorder) - 1)