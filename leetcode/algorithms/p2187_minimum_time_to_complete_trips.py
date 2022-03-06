from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 1, min(time) * totalTrips

        while left < right:
            middle = left + (right - left) // 2
            current_trips = sum([middle // x for x in time])

            if current_trips < totalTrips:
                left = middle + 1
            else:
                right = middle

        return left
