from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        return self._build(preorder, 0, len(preorder) - 1)

    def _build(self, preorder: List[int], start: int, end: int) -> TreeNode:
        if start > end:
            return None

        root_value = preorder[start]
        right_tree_start = next(
            (i for i in range(start, end + 1) if preorder[i] > root_value),
            end + 1)

        root = TreeNode(root_value)
        root.left = self._build(preorder, start + 1, right_tree_start - 1)
        root.right = self._build(preorder, right_tree_start, end)

        return root
