from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self._at_most_k(nums, k) - self._at_most_k(nums, k - 1)

    def _at_most_k(self, nums, k):
        start, count = 0, 0
        odd_count = 0

        for end, n in enumerate(nums):
            if n & 1 == 1:
                odd_count += 1

            while odd_count > k:
                if nums[start] & 1 == 1:
                    odd_count -= 1

                start += 1

            count += end - start + 1

        return count
