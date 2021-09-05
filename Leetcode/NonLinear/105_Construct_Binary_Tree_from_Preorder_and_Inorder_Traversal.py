from typing import List, Optional

from Leetcode.NonLinear import _tree_input


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            # 전위 순회 결과는 중위 순회 분할 인덱스
            index = inorder.index(preorder.pop(0))

            # 중위 순회 결과 분할 정복
            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[0:index])
            node.right = self.buildTree(preorder, inorder[index + 1:])

            return node


if __name__ == "__main__":
    t = Solution()
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    # root = _tree_input.input_order(root)

    root = t.buildTree(preorder, inorder)
    _tree_input.preOrder(root)