import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = []
        counts = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heapq.heapify(counts)

        while len(counts) > 1:
            c1, l1 = heapq.heappop(counts)
            c2, l2 = heapq.heappop(counts)

            if c1 == c2:
                result.extend([l1, l2])
                c1 += 1
                c2 += 1
            else:
                result.extend([l1, l1, l2])
                c1 += 2
                c2 += 1

            if c1 < 0:
                heapq.heappush(counts, (c1, l1))

            if c2 < 0:
                heapq.heappush(counts, (c2, l2))

        if counts:
            count, char = heapq.heappop(counts)
            result.extend([char] * min(2, -count))

        return ''.join(result)
