import collections
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        values = collections.deque([])
        queue = [root]

        while queue:
            node = queue.pop()
            values.appendleft(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return list(values)
