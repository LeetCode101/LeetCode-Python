import collections
import heapq


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s)
        heap = [(-count, c) for c, count in counter.items()]
        heapq.heapify(heap)
        result = ''

        while heap:
            count, c = heapq.heappop(heap)
            result += c * -count

        return result
