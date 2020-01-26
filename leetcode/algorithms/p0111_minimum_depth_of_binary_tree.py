from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        queue = deque([root]) if root else deque()
        depth = 0

        while queue:
            depth += 1
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()

                if not node.left and not node.right:
                    return depth

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return depth
