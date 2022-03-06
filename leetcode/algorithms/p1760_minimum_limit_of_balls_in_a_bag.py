import heapq
from typing import List


# Time Limit Exceeded!
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)

        while left < right:
            middle = left + (right - left) // 2
            current_operations = self._count_operations(
                nums, middle, maxOperations)

            if current_operations > maxOperations:
                left = middle + 1
            else:
                right = middle

        return left

    def _count_operations(self, nums, penalty, max_operations):
        heap = [-x for x in nums]
        heapq.heapify(heap)
        operations = 0

        while heap and -heap[0] > penalty:
            top = -heapq.heappop(heap)

            heapq.heappush(heap, -penalty)
            heapq.heappush(heap, penalty - top)
            operations += 1

            if operations > max_operations:
                break

        return operations
