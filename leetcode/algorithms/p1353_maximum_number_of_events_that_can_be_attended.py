import heapq
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        if not events:
            return 0

        sorted_events = sorted(events)
        total_days = max(event[1] for event in events)
        heap = []
        i = 0
        day = 1
        count = 0

        while day <= total_days:
            if i < len(sorted_events) and not heap:
                day = sorted_events[i][0]

            while i < len(sorted_events) and sorted_events[i][0] <= day:
                heapq.heappush(heap, sorted_events[i][1])
                i += 1

            while heap and heap[0] < day:
                heapq.heappop(heap)

            if heap:
                heapq.heappop(heap)
                count += 1
            elif i >= len(sorted_events):
                break

            day += 1

        return count
