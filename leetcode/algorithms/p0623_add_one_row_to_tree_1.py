import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) \
            -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)

        queue = collections.deque([root])
        current_depth = 0

        while queue:
            current_depth += 1
            size = len(queue)

            if current_depth + 1 == depth:
                for _ in range(size):
                    node = queue.popleft()
                    node.left = TreeNode(val, node.left)
                    node.right = TreeNode(val, None, node.right)

                return root

            for _ in range(size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return root
