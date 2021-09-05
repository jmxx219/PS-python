from typing import Optional

import _tree_input


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        longest = 0

        def dfs(node: TreeNode) -> int:
            if not node:
                return 0

            nonlocal longest

            left = dfs(node.left)
            right = dfs(node.right)

            longest = max(longest, left + right)
            return max(left, right) + 1

        dfs(root)
        return longest


if __name__ == "__main__":
    t = Solution()
    root = []
    root = _tree_input.input_order(root)
    print(t.diameterOfBinaryTree(root))