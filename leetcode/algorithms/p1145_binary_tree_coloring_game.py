from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) \
            -> bool:
        current = root
        stack = [current]

        while current:
            node = stack.pop()

            if node.val == x:
                current = node

                break

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        sub_tree_count = self._count(n, current)
        sub_tree_left_count = self._count(n, current.left) \
            if current.left else 0
        sub_tree_right_count = sub_tree_count - sub_tree_left_count - 1
        max_count = max(n - sub_tree_count,
                        sub_tree_left_count, sub_tree_right_count)

        return max_count >= n / 2

    def _count(self, n, root):
        count = 0
        stack = [root]

        while stack:
            node = stack.pop()
            count += 1

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return count
