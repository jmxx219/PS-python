from typing import Optional

from Leetcode.NonLinear import _tree_input


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution: # 브루트포스
    sum_range = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root.left: self.rangeSumBST(root.left, low, high)
        if low <= root.val <= high: self.sum_range += root.val
        if root.right: self.rangeSumBST(root.right, low, high)
        return self.sum_range


class Solution2: # 가지치기
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node: TreeNode):
            if not node:
                return 0

            if node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)
            return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)


if __name__ == "__main__":
    t = Solution()
    root = [10,5,15,3,7,None,18]
    low = 7
    high = 15
    root = _tree_input.input_order(root)
    print(t.rangeSumBST(root, low, high))