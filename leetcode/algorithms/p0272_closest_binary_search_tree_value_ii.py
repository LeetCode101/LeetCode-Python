# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) \
            -> List[int]:
        sorted_values = []
        self._preorder_traversal(root, sorted_values)

        return self._find_closest_elements(sorted_values, k, target)

    def _preorder_traversal(self, root: TreeNode, values: List[int]) -> None:
        if not root:
            return

        self._preorder_traversal(root.left, values)

        values.append(root.val)

        self._preorder_traversal(root.right, values)

    def _find_closest_elements(self, arr: List[int], k: int, x: float) \
            -> List[int]:
        low, high = 0, len(arr) - k

        while low < high:
            middle = low + (high - low) // 2

            if x - arr[middle] > arr[middle + k] - x:
                low = middle + 1
            else:
                high = middle

        return arr[low:low + k]
