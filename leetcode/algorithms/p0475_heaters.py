import bisect
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        radius = 0
        n = len(heaters)
        sorted_heaters = sorted(heaters)

        for house in houses:
            i = bisect.bisect_left(sorted_heaters, house)

            if i == 0:
                radius = max(radius, abs(house - sorted_heaters[0]))
            elif i == n:
                radius = max(radius, abs(house - sorted_heaters[-1]))
            else:
                radius = max(radius, min(abs(house - sorted_heaters[i - 1]),
                                         abs(house - sorted_heaters[i])))

        return radius
