from typing import Set


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) \
            -> bool:
        nums = set()

        self.traverse(root1, nums)

        return self.find(root2, target, nums)

    def traverse(self, root: TreeNode, nums: Set[int]):
        if not root:
            return

        nums.add(root.val)

        self.traverse(root.left, nums)
        self.traverse(root.right, nums)

    def find(self, root: TreeNode, k: int, visited: Set[int]) -> bool:
        if not root:
            return False

        if k - root.val in visited:
            return True

        return self.find(root.left, k, visited) or self.find(
            root.right, k, visited)
