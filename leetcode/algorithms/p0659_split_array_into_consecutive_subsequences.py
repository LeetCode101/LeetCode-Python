import collections
from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        counter = collections.Counter(nums)
        next_numbers = collections.defaultdict(int)

        for n in nums:
            if counter[n] == 0:
                continue

            if next_numbers[n] > 0:
                next_numbers[n] -= 1
                next_numbers[n + 1] += 1
            elif counter[n + 1] > 0 and counter[n + 2] > 0:
                counter[n + 1] -= 1
                counter[n + 2] -= 1
                next_numbers[n + 3] += 1
            else:
                return False

            counter[n] -= 1

        return True
