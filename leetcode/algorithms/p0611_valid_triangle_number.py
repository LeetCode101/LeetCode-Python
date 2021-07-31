from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        count = 0

        for i in range(len(sorted_nums) - 1, 1, -1):
            low, high = 0, i - 1

            while low < high:
                if sorted_nums[low] + sorted_nums[high] > sorted_nums[i]:
                    count += high - low
                    high -= 1
                else:
                    low += 1

        return count
