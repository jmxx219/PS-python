import collections
from sys import stdin


class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(node):
    print(node.val, end="")
    if node.left != ".": preorder(tree[node.left])
    if node.right != ".": preorder(tree[node.right])


def inorder(node):
    if node.left != ".": inorder(tree[node.left])
    print(node.val, end="")
    if node.right != ".": inorder(tree[node.right])


def postorder(node):
    if node.left != ".": postorder(tree[node.left])
    if node.right != ".": postorder(tree[node.right])
    print(node.val, end="")


N = int(stdin.readline())
tree = {}
for _ in range(N):
    a, b, c = map(str, stdin.readline().strip().split())
    tree[a] = TreeNode(a, b, c)
preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])
print()
