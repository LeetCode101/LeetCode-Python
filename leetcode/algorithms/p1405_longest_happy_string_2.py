import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = []
        counts = [(-count, char) for count, char in
                  [(a, 'a'), (b, 'b'), (c, 'c')] if count > 0]
        heapq.heapify(counts)

        while len(counts) > 1:
            count1, char1 = heapq.heappop(counts)
            count2, char2 = heapq.heappop(counts)

            if count1 == count2:
                result.extend([char1, char2])
                count1 += 1
                count2 += 1
            else:
                result.extend([char1, char1, char2])
                count1 += 2
                count2 += 1

            if count1 < 0:
                heapq.heappush(counts, (count1, char1))

            if count2 < 0:
                heapq.heappush(counts, (count2, char2))

        if counts:
            count, char = heapq.heappop(counts)
            result.extend([char] * min(2, -count))

        return ''.join(result)
