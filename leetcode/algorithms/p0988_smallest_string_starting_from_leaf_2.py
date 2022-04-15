import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        paths = []
        queue = collections.deque([(root, '')])

        while queue:
            node, path = queue.popleft()
            path += chr(node.val + 97)

            if node.left:
                queue.append((node.left, path))

            if node.right:
                queue.append((node.right, path))

            if not node.left and not node.right:
                paths.append(path[::-1])

        return sorted(paths)[0]
