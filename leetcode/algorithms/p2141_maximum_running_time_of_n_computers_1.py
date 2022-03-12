import heapq
from typing import List


# Time Limit Exceeded!
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        heap = [-x for x in batteries]
        heapq.heapify(heap)
        time = 0

        while heap:
            current_batteries = []

            for _ in range(n):
                if not heap:
                    return time

                remaining_battery_time = -heapq.heappop(heap) - 1

                if remaining_battery_time > 0:
                    current_batteries.append(remaining_battery_time)

            time += 1

            for battery in current_batteries:
                heapq.heappush(heap, -battery)

        return time
