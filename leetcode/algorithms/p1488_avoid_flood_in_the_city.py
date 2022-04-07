import bisect
import collections
from typing import List


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        result = [-1] * n
        zeros = []
        waters = collections.defaultdict(int)

        for i, lake in enumerate(rains):
            if lake == 0:
                zeros.append(i)
                result[i] = 1
            else:
                if lake in waters:
                    j = bisect.bisect_left(zeros, waters[lake])

                    if j == len(zeros):
                        return []

                    result[zeros.pop(j)] = lake

                waters[lake] = i

        return result
