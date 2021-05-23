import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = collections.Counter(nums)
        sort_by_frequency = sorted(list(frequencies.items()),
                                   key=lambda x: x[1], reverse=True)

        return list(map(lambda x: x[0], sort_by_frequency))[:k]
