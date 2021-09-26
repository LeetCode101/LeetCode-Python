import collections
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = collections.Counter(s)
        counts = []
        result = []

        for key, count in counter.items():
            counts.append((-count, key))

        heapq.heapify(counts)

        while len(counts) > 1:
            count1, char1 = heapq.heappop(counts)
            count2, char2 = heapq.heappop(counts)

            result.extend([char1, char2])
            count1 += 1
            count2 += 1

            if count1 < 0:
                heapq.heappush(counts, (count1, char1))

            if count2 < 0:
                heapq.heappush(counts, (count2, char2))

        if counts:
            if -counts[-1][0] == 1:
                result.append(counts[-1][1])
            else:
                return ''

        return ''.join(result)
