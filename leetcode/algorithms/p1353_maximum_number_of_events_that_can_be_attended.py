import heapq
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        if not events:
            return 0

        heap = [(start, end) for start, end in events]
        heapq.heapify(heap)
        prev, _ = heapq.heappop(heap)
        count = 1

        while heap:
            while heap and heap[0][0] <= prev <= heap[0][1]:
                start, end = heapq.heappop(heap)
                heapq.heappush(heap, (prev + 1, end))

                if start == end:
                    break

            start, end = heapq.heappop(heap)
            count += 1 if prev < end else 0
            prev = start

        return count
