from heapq import heappush, heappop
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap = []

        for i in range(min(k, len(matrix))):
            heappush(min_heap, (matrix[i][0], 0, matrix[i]))

        for _ in range(k - 1):
            number, i, row = heappop(min_heap)

            if len(row) > i + 1:
                heappush(min_heap, (row[i + 1], i + 1, row))

        return min_heap[0][0]
