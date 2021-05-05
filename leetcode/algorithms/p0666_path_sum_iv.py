from typing import List


class Solution:
    def pathSum(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nodes = {}

        for n in nums:
            nodes[n // 10] = n % 10

        return self._dfs(nums[0] // 10, 0, nodes)

    def _dfs(self, root, sum_so_far, nodes):
        if root not in nodes:
            return 0

        depth = root // 10
        position = root % 10
        left = (depth + 1) * 10 + position * 2 - 1
        right = left + 1
        sum_so_far += nodes.get(root, 0)

        if left not in nodes and right not in nodes:
            return sum_so_far

        return self._dfs(left, sum_so_far, nodes) \
            + self._dfs(right, sum_so_far, nodes)
