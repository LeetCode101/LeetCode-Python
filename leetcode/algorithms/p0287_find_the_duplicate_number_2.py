from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 1, len(nums) - 1

        while low < high:
            middle = low + (high - low) // 2
            count = 0

            for n in nums:
                if n <= middle:
                    count += 1

            if count <= middle:
                low = middle + 1
            else:
                high = middle

        return low
