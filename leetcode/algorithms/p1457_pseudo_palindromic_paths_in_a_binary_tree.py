import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time Limit Exceeded!
class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, [])]
        count = 0

        while stack:
            node, prev_values = stack.pop()
            values = prev_values + [node.val]

            if self._is_leaf(node) and self._is_palindromic(values):
                count += 1

            if node.left:
                stack.append((node.left, values))

            if node.right:
                stack.append((node.right, values))

        return count

    def _is_leaf(self, node):
        return not node.left and not node.right

    def _is_palindromic(self, values):
        has_odd = False
        counter = collections.Counter(values)

        for count in counter.values():
            if count & 1 == 1:
                if has_odd:
                    return False

                has_odd = True

        return True
