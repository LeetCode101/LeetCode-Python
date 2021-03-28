from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1

        while low <= high:
            middle = low + (high - low) // 2

            if nums[middle] > target:
                high = middle - 1
            elif nums[middle] < target:
                low = middle + 1
            else:
                start, end = middle, middle

                while start >= 0 and nums[start] == target:
                    start -= 1

                while end < len(nums) and nums[end] == target:
                    end += 1

                return [start + 1, end - 1]

        return [-1, -1]
