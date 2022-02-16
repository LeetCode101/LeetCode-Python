import heapq
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        if not events:
            return 0

        heap = []
        count = 0
        i, n = 0, len(events)
        sorted_events = sorted(events, key=lambda x: x[0])
        day = 0

        while i < n or heap:
            if not heap:
                day = sorted_events[i][0]

            while i < n and sorted_events[i][0] <= day:
                heapq.heappush(heap, sorted_events[i][1])
                i += 1

            heapq.heappop(heap)
            count += 1
            day += 1

            while heap and heap[0] < day:
                heapq.heappop(heap)

        return count
