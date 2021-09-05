from typing import Optional

from Leetcode.NonLinear import _tree_input


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    check: bool = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def depth(node: TreeNode) -> int:
            if node is None:
                return 0
            else:
                l = depth(node.left)
                r = depth(node.right)
                if abs(l - r) > 1:
                    self.check = False
                return max(l, r) + 1

        depth(root)
        return self.check

    def isBalanced2(self, root: TreeNode) -> bool:
        def check(root):
            if not root:
                return 0

            left = check(root.left)
            right = check(root.right)
            # 높이 차이가 나는 경우 -1, 이외에는 높이에 따라 1 증가
            if left == -1 or \
                    right == -1 or \
                    abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return check(root) != -1


if __name__ == "__main__":
    t = Solution()
    root = [1, 2, 2, 3, None, None, 3, 4, None, None, 4]
    root = _tree_input.input_order(root)
    print(t.isBalanced(root))
