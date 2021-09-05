from typing import Optional

import _tree_input


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2 :
            return

        if root1 and root2:
            root1.val += root2.val
        elif root2:
            root1 = TreeNode(root2.val)

        if root1 and root2:
            root1.left = self.mergeTrees(root1.left, root2.left)
            root1.right = self.mergeTrees(root1.right, root2.right)

        return root1

    def mergeTrees2(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            node = TreeNode(t1.val + t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)

            return node
        else:
            return t1 or t2


if __name__ == "__main__":
    t = Solution()
    root1 = [1,3,2,5]
    root2 = [2,1,3,None,4,None,7]
    root1 = _tree_input.input_order(root1)
    root2 = _tree_input.input_order(root2)
    _tree_input.preOrder(t.mergeTrees(root1, root2))