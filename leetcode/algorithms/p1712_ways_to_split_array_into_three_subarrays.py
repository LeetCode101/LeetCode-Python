from typing import List


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        prefix_sum = [0]

        for n in nums:
            prefix_sum.append(prefix_sum[-1] + n)

        count = 0
        j = k = 0

        for i in range(1, len(nums)):
            j = max(j, i + 1)

            while j < len(nums) and 2 * prefix_sum[i] > prefix_sum[j]:
                j += 1

            k = max(k, j)

            while k < len(nums) \
                    and 2 * prefix_sum[k] <= prefix_sum[i] + prefix_sum[-1]:
                k += 1

            count += k - j

        return count % 1_000_000_007
