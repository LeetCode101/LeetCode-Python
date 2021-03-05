from typing import List


# Time complexity: O(nlgn)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        high = len(nums) - 1

        for index, value in enumerate(nums):
            """
            Find the minimum index j such that
            nums[j] >= target - value for all x in [j, len(nums) - 1]
            """
            j = self._binary_search(nums, index + 1, high, target - value)

            if j == -1:
                continue

            if value + nums[j] == target:
                return [index + 1, j + 1]

            high = j

        return [-1, -1]

    def _binary_search(
            self, nums: List[int], low: int, high: int, target: int) -> int:
        while low <= high:
            middle = (low + high) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                low = middle + 1
            elif middle - 1 >= low and nums[middle - 1] >= target:
                high = middle - 1
            else:
                return middle

        return -1
