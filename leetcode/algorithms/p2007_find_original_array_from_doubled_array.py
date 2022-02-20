import collections
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counter = collections.Counter(changed)
        keys = sorted(counter.keys(), key=abs)
        result = []
        zeros = counter[0]

        for n in keys:
            if n != 0 and counter[n * 2] > 0 and counter[n * 2] >= counter[n]:
                result.extend([n] * counter[n])
                counter[n * 2] -= counter[n]
                counter[n] = 0

        if zeros > 0 and zeros & 1 == 0:
            result.extend([0] * (zeros >> 1))

        return result if len(result) * 2 == len(changed) else []
