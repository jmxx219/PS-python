from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def input_order(input_list: List):
    if not input_list:
        return None
    root = parent = TreeNode(input_list[0])
    index = 0
    parent.left = __input_order(parent, index * 2 + 1, input_list)
    parent.right = __input_order(parent, index * 2 + 2, input_list)
    return root


def __input_order(parent: TreeNode, index: int, input_list: List):
    if index >= len(input_list) or input_list[index] == None:
        return None
    curr = TreeNode(input_list[index])
    curr.left = __input_order(curr, index * 2 + 1, input_list)
    curr.right = __input_order(curr, index * 2 + 2, input_list)
    return curr

def preOrder(root: TreeNode):
    if root:
        print(root.val, end=" ")
        preOrder(root.left)
        preOrder(root.right)


if __name__ == "__main__":
    root = [3, 9, 20, None, None, 15, 7]
    root = input_order(root)
    preOrder(root)