import collections

from Leetcode.NonLinear import _tree_input


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        treeList = []

        def preorder(node: TreeNode) -> None:
            if not node:
                treeList.append("N")  # for null
            else:
                treeList.append(str(node.val))
                preorder(node.left)
                preorder(node.right)

        preorder(root)
        return " ".join(treeList)

    def deserialize(self, data: str) -> TreeNode:

        def preorderDe() -> TreeNode:
            val = next(treeIter)
            if val == "N": return None
            node = TreeNode(int(val))
            node.left = preorderDe()
            node.right = preorderDe()
            return node

        treeIter = iter(data.split())
        return preorderDe()


class Codec2:

    def serialize(self, root: TreeNode) -> str: # 직렬화(트리를 단일 문자열로)
        queue = collections.deque([root])
        result = ['#']
        # 트리 BFS 직렬화
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)

                result.append(str(node.val))
            else:
                result.append('#')
        return ' '.join(result)

        # 역직렬화

    def deserialize(self, data: str) -> TreeNode:
        # 예외 처리
        if data == '# #':
            return None

        nodes = data.split()

        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])
        index = 2
        # 빠른 런너처럼 자식 노드 결과 먼저 확인 후 큐 삽입
        while queue:
            node = queue.popleft()
            if nodes[index] is not '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            if nodes[index] is not '#':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        return root


if __name__ == "__main__":
    ser = Codec()
    deser = Codec()
    root = [1,2,3,None,None,4,5]
    root = _tree_input.input_order(root)
    ans = ser.serialize(root)
    # ans = deser.deserialize(ser.serialize(root))
    print(ans)