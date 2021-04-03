import collections
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) \
            -> List[int]:
        deque = collections.deque([])
        self._inorder_traversal(root, deque)

        while len(deque) > k:
            if abs(deque[0] - target) > abs(deque[-1] - target):
                deque.popleft()
            else:
                deque.pop()

        return list(deque)

    def _inorder_traversal(self, root: TreeNode, deque) -> None:
        if not root:
            return

        self._inorder_traversal(root.left, deque)

        deque.append(root.val)

        self._inorder_traversal(root.right, deque)
