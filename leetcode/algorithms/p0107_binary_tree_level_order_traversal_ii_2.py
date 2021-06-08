from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        queue = deque()

        self._dfs(root, 1, queue)

        return list(queue)

    def _dfs(self, root: TreeNode, level: int,
             queue: List[List[int]]) -> None:
        if not root:
            return

        if level > len(queue):
            queue.appendleft([])

        queue[-level].append(root.val)

        self._dfs(root.left, level + 1, queue)
        self._dfs(root.right, level + 1, queue)
