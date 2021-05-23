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
            left_size = k - len(topK)

            if left_size <= 0:
                break

            if bucket[i]:
                topK += bucket[i][:min(len(bucket[i]), left_size)]

        return topK
