import collections
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self._at_most_k(nums, k) - self._at_most_k(nums, k - 1)

    def _at_most_k(self, nums, k):
        counter = collections.defaultdict(int)
        count = 0
        start = 0

        for end, n in enumerate(nums):
            counter[n] += 1

            while len(counter) > k:
                counter[nums[start]] -= 1

                if counter[nums[start]] == 0:
                    counter.pop(nums[start])

                start += 1

            count += end - start + 1

        return count
