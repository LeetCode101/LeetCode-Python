import collections
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counter = collections.Counter(changed)
        keys = sorted(counter.keys())
        result = []

        for n in keys:
            if n == 0 or counter[n * 2] == 0:
                continue

            if counter[n * 2] >= counter[n]:
                result.extend([n] * counter[n])
                counter[n * 2] -= counter[n]
                counter[n] = 0

        if counter[0] > 0 and counter[0] & 1 == 0:
            result.extend([0] * (counter[0] >> 1))

        return result if len(result) * 2 == len(changed) else []
