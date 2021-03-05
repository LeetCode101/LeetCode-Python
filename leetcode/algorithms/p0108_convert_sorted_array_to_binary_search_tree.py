from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self._build_tree(nums, 0, len(nums) - 1)

    def _build_tree(self, nums: List[int], low: int, high: int) -> TreeNode:
        if low > high:
            return None

        middle = (low + high) // 2
        root = TreeNode(nums[middle])
        root.left = self._build_tree(nums, low, middle - 1)
        root.right = self._build_tree(nums, middle + 1, high)

        return root
