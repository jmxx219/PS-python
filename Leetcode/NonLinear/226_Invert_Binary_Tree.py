from typing import Optional

from Leetcode.NonLinear import _tree_input
from Leetcode.NonLinear._tree_input import preOrder


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root


if __name__ == "__main__":
    t = Solution()
    root = []
    root = _tree_input.input_order(root)
    preOrder(t.invertTree(root))