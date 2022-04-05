import collections
from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        length = nums[-1] - nums[0] + 1
        buckets = [0] * length
        counter = collections.Counter(nums)
        shift = nums[0]

        for n, count in counter.items():
            buckets[n - shift] = count

        while True:
            i = 0

            while i < length and buckets[i] == 0:
                i += 1

            if i == length:
                break

            count = 1
            base = buckets[i]
            buckets[i] = 0
            i += 1
            prev_count = 0

            while i < length and buckets[i] != 0:
                if buckets[i] >= base and buckets[i] - base >= prev_count:
                    buckets[i] -= base
                    count += 1
                else:
                    break

                prev_count = buckets[i]
                i += 1

            if count < 3:
                return False

        return True
