import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        order = []
        queue = collections.deque([(1, root)])
        next_level = 1

        while queue:
            level, node = queue.popleft()

            if level == next_level:
                order.append(node.val)
                next_level += 1

            if node.right:
                queue.append((level + 1, node.right))

            if node.left:
                queue.append((level + 1, node.left))

        return order
