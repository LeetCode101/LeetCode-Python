from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        n = len(nums)

        if n < k or total % k != 0:
            return False

        sums = [0] * k
        sorted_nums = sorted(nums, reverse=True)

        return self._dfs(sorted_nums, sums, 0, k, total // k)

    def _dfs(self, nums, sums, start, k, target):
        if start == len(nums):
            return True

        for i in range(k):
            sums[i] += nums[start]

            if sums[i] <= target and self._dfs(
                    nums, sums, start + 1, k, target):
                return True

            sums[i] -= nums[start]

            if sums[i] == 0:
                break

        return False
