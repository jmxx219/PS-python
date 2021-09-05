from typing import List, Optional

from Leetcode.NonLinear import _tree_input


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.head = None

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def balance(lo: int, hi: int, node: TreeNode):
            if lo == hi:
                return TreeNode(nums[lo])
            if lo > hi:
                return None
            mid = (hi+lo) // 2
            node = TreeNode(nums[mid])
            node.left = balance(lo, mid - 1, node.left)
            node.right = balance(mid + 1, hi, node.right)
            return node

        self.head = balance(0, len(nums)-1, self.head)
        return self.head


if __name__ == "__main__":
    t = Solution()
    nums = [-10,-3,0,5,9]
    root = t.sortedArrayToBST(nums)
    print(_tree_input.preOrder(root))