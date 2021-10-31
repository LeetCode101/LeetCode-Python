import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        depth = 1
        queue = collections.deque([(root, 1)])

        while queue:
            size = len(queue)

            for i in range(size):
                node, id = queue.popleft()

                if id != pow(2, depth - 1) + i:
                    return False

                if node.left:
                    queue.append((node.left, id * 2))

                if node.right:
                    queue.append((node.right, id * 2 + 1))

            if len(queue) > 0 and size != pow(2, depth - 1):
                return False

            depth += 1

        return True
