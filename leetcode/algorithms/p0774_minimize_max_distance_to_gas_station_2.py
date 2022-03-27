import math
from typing import List


class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        left, right = 0, stations[-1] - stations[0]
        n = len(stations)

        while left + 1e-6 < right:
            middle = left + (right - left) / 2
            count = 0

            for i in range(n - 1):
                distance = stations[i + 1] - stations[i]
                count += math.ceil(distance / middle) - 1

            if count > k:
                left = middle
            else:
                right = middle

        return right
