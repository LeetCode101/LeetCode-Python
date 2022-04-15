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
        queue = collections.deque([(root, '')])
        min_path = ''

        while queue:
            node, path = queue.popleft()
            path += chr(node.val + 97)

            if node.left:
                queue.append((node.left, path))

            if node.right:
                queue.append((node.right, path))

            if not node.left and not node.right:
                min_path = path[::-1] if not min_path \
                    else min(min_path, path[::-1])

        return min_path
