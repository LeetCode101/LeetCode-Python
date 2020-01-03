from typing import List


# Time Limit Exceeded!
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = [0] * len(nums)
        sum = 0
        count = 0

        for i, value in enumerate(nums):
            sum += value
            sums[i] = sum

        for i in range(len(nums)):
            if nums[i] == k:
                count += 1

            for j in range(i + 1, len(nums)):
                if sums[j] - sums[i] + nums[i] == k:
                    count += 1

        return count
