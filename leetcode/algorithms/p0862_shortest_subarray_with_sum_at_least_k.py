import heapq
import sys
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        heap, min_length, sum_so_far = [], sys.maxsize, 0
        heapq.heappush(heap, (0, -1))

        for i, num in enumerate(nums):
            sum_so_far += num
            diff = sum_so_far - k

            while heap and \
                    (heap[0][0] <= diff or i - heap[0][1] >= min_length):
                pre_sum, pre_index = heapq.heappop(heap)

                if i - pre_index < min_length:
                    min_length = i - pre_index

            heapq.heappush(heap, (sum_so_far, i))

        return min_length < sys.maxsize and min_length or -1
