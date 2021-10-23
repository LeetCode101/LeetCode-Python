import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        nodes = []
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()

            if (node.left and not node.right) \
                    or (node.right and not node.left):
                nodes.append(node.left.val if node.left else node.right.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return nodes
