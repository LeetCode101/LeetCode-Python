from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        low, high = max(nums), sum(nums)

        while low < high:
            middle = low + (high - low) // 2

            if self._has_more_than_m_groups(nums, middle, m):
                low = middle + 1
            else:
                high = middle

        return low

    def _has_more_than_m_groups(self, nums: List[int],
                                largest_sum: int, m: int) -> bool:
        current = 0

        for num in nums:
            if current + num > largest_sum:
                m -= 1

                if m <= 0:
                    return True

                current = num
            else:
                current += num

        return False
