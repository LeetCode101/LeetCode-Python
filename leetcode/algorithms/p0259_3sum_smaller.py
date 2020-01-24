from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0

        for i in range(0, len(nums) - 2):
            k = target - nums[i]
            low, high = i + 1, len(nums) - 1

            while low < high:
                if nums[low] + nums[high] < k:
                    count += high - low
                    low += 1
                else:
                    high -= 1

        return count
