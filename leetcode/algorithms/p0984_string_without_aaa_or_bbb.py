import heapq


class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        heap = [(-a, 'a'), (-b, 'b')]
        heapq.heapify(heap)
        result = []

        while len(heap) > 1:
            count1, char1 = heapq.heappop(heap)
            count2, char2 = heapq.heappop(heap)

            if count1 == count2:
                result.extend([char1, char2])
                count1 += 1
                count2 += 1
            else:
                result.extend([char1, char1, char2])
                count1 += 2
                count2 += 1

            if count1 < 0:
                heapq.heappush(heap, (count1, char1))

            if count2 < 0:
                heapq.heappush(heap, (count2, char2))

        if heap:
            count, char = heapq.heappop(heap)
            result.extend([char] * -count)

        return ''.join(result)
