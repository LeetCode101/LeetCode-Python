import collections
import math
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = collections.Counter(nums)
        buckets = [[] for _ in range(max(counter.values()))]
        result = []

        for n, count in counter.items():
            buckets[count - 1].append(n)

        target = len(nums) / 3
        start = math.ceil(target) if math.floor(target) < target else target + 1

        for i in range(int(start) - 1, len(buckets)):
            result.extend(buckets[i])

        return result
