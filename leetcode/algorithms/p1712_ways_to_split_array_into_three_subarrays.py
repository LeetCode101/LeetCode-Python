from typing import List


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        prefix_sum = [n for n in nums]

        for i in range(1, len(nums)):
            prefix_sum[i] = nums[i] + prefix_sum[i - 1]

        count = 0
        j = k = 0

        for i in range(len(nums) - 2):
            j = max(j, i + 1)

            while j < len(nums) - 1 and prefix_sum[i] \
                    > prefix_sum[j] - prefix_sum[i]:
                j += 1

            k = max(k, j)

            while k < len(nums) - 1 and prefix_sum[k] - prefix_sum[i] \
                    <= prefix_sum[-1] - prefix_sum[k]:
                k += 1

            count = (count + k - j) % 1000000007

        return count
