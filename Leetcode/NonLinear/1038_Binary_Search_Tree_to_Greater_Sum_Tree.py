from Leetcode.NonLinear import _tree_input


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.sum_node = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root.right: self.bstToGst(root.right)
        self.sum_node += root.val
        root.val = self.sum_node
        if root.left: self.bstToGst(root.left)
        return root


if __name__ == "__main__":
    t = Solution()
    root = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
    root = _tree_input.input_order(root)
    # t.bstToGst(root)
    _tree_input.preOrder(t.bstToGst(root))