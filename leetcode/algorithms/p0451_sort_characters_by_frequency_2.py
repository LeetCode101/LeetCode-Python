import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s)
        buckets = [[] for _ in range(max(counter.values()))]
        result = ''

        for c, count in counter.items():
            buckets[count - 1].append(c)

        for i in range(len(buckets) - 1, -1, -1):
            for c in buckets[i]:
                result += c * (i + 1)

        return result
