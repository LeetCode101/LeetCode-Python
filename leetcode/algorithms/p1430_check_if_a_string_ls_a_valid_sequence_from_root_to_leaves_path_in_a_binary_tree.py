import collections
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) \
            -> bool:
        n = len(arr)
        queue = collections.deque([(root, 0)])

        while queue:
            node, start = queue.popleft()

            if start < n and arr[start] == node.val:
                if node.left:
                    queue.append((node.left, start + 1))

                if node.right:
                    queue.append((node.right, start + 1))

                if not node.left and not node.right and start + 1 == n:
                    return True

        return False
