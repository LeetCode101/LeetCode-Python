import collections
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = collections.Counter(nums)
        result = []
        buckets = [[] for _ in range(max(counter.values()))]

        for n, count in counter.items():
            buckets[count - 1].append(n)

        for i in range(len(buckets)):
            for n in sorted(buckets[i], reverse=True):
                result.extend([n] * (i + 1))

        return result
