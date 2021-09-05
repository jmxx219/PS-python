import math
import sys
from typing import Optional
from Leetcode.NonLinear import _tree_input


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    prev = -sys.maxsize
    res = sys.maxsize
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root.left:
            self.minDiffInBST(root.left)
        self.res = min(self.res, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.res

    def minDiffInBST(self, root: TreeNode) -> int:
        def dfs(node, prev):
            if not node:
                return prev

            prev = dfs(node.left, prev)

            if prev is not None:
                self.min_dist = min(self.min_dist, node.val - prev)

            return dfs(node.right, node.val)

        self.min_dist = math.inf
        dfs(root, None)

        return self.min_dist


if __name__ == "__main__":
    t = Solution()
    root = [90,69,None,49,89,None,52]
    root = _tree_input.input_order(root)
    # _tree_input.preOrder(root)
    print(t.minDiffInBST(root))