import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        sums = collections.defaultdict(int)
        frequent_sums = []
        max_frequency = 0

        self._dfs(root, sums)

        for frequency in sums.values():
            max_frequency = max(max_frequency, frequency)

        for sum, frequency in sums.items():
            if max_frequency == frequency:
                frequent_sums.append(sum)

        return frequent_sums

    def _dfs(self, root, sums):
        if not root:
            return 0

        current_sum = root.val + self._dfs(root.left, sums) \
            + self._dfs(root.right, sums)
        sums[current_sum] += 1

        return current_sum
