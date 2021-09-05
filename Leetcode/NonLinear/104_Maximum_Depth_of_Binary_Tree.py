
import collections
import _tree_input


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1
            # 큐 연산 추출 노드의 자식 노드 삽입
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
        # BFS 반복 횟수 == 깊이
        return depth

    def maxDepth2(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return max(self.maxDepth2(root.left), self.maxDepth2(root.right)) + 1


if __name__ == "__main__":
    t = Solution()
    root = [3, 9, 20, None, None, 15, 7]
    root = _tree_input.input_order(root)
    print(t.maxDepth(root))
    print(t.maxDepth2(root))