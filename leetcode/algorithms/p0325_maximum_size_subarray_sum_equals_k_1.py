from typing import List


# Time Limit Exceeded!
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        max_length = 0
        sums = [0] * len(nums)

        for i, n in enumerate(nums):
            sums[i] = sums[i - 1] + n if i != 0 else n

        for i in range(len(nums)):
            if sums[i] == k:
                max_length = max(max_length, i + 1) \
                    if max_length != 0 else (i + 1)

            for j in range(i + 1, len(nums)):
                if sums[j] - sums[i] == k:
                    current_length = j - i
                    max_length = max(max_length, current_length) \
                        if max_length != 0 else current_length

        return max_length
