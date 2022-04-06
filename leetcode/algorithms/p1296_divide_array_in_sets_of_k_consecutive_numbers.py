import collections
from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        counter = collections.Counter(nums)

        for n in sorted(nums):
            if counter[n] == 0:
                continue

            for i in range(n, n + k):
                if counter[i] == 0:
                    return False

                counter[i] -= 1

        return True
