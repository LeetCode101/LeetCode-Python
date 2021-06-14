from typing import List


# Time Limit Exceeded!
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.count = 0


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        counts = [0]
        root = TreeNode(nums[-1])

        for i in range(len(nums) - 2, -1, -1):
            count = self._insert(root, nums[i])
            counts.append(count)

        return list(reversed(counts))

    def _insert(self, root, value):
        count = 0
        prev, current = None, root

        while current:
            prev = current

            if current.value < value:
                count += current.count + 1
                current = current.right
            else:
                current.count += 1
                current = current.left

        if prev.value < value:
            prev.right = TreeNode(value)
        else:
            prev.left = TreeNode(value)

        return count
