import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        frequencies = collections.Counter(nums)

        for n, frequency in frequencies.items():
            bucket[frequency].append(n)

        topK = []

        for i in range(len(nums), -1, -1):
            if len(topK) == k:
                break

            if bucket[i]:
                topK += bucket[i]

        return topK
