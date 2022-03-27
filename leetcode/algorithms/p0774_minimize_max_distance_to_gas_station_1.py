import heapq
from typing import List


# Time Limit Exceeded!
class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        gaps = []
        heapq.heapify(gaps)

        for i in range(1, len(stations)):
            gap = stations[i] - stations[i - 1]
            heapq.heappush(gaps, (-gap, gap, 1))

        while k > 0:
            _, gap, count = heapq.heappop(gaps)
            heapq.heappush(gaps, (-gap / (count + 1), gap, count + 1))
            k -= 1

        return -gaps[0][0]
