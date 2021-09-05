from typing import List, Optional

from Leetcode.NonLinear import _tree_input


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            node = TreeNode(postorder.pop())
            index = inorder.index(node.val)

            node.right = self.buildTree(inorder[index + 1:], postorder)
            node.left = self.buildTree(inorder[0:index], postorder)

            return node


if __name__ == "__main__":
    t = Solution()
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]

    root = t.buildTree(inorder, postorder)
    _tree_input.preOrder(root)