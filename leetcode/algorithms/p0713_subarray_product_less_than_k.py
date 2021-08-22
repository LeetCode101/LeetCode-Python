from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        count = 0
        product = 1
        start = 0

        for end, n in enumerate(nums):
            product *= n

            while product >= k and start <= end:
                product //= nums[start]
                start += 1

            count += end - start + 1

        return count
