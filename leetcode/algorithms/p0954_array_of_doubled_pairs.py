import collections
from typing import List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        counter = collections.Counter(arr)
        keys = sorted(counter.keys())

        for n in sorted(keys, key=lambda x: abs(x)):
            if counter[n] > counter[2 * n]:
                return False

            counter[2 * n] -= counter[n]

        return True
