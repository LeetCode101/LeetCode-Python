import collections
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        bucket = [[] for _ in range(len(words) + 1)]
        frequencies = collections.Counter(words)

        for word, frequency in frequencies.items():
            bucket[frequency].append(word)

        for w in bucket:
            if w:
                w.sort()

        top_k = []

        for i in range(len(words), -1, -1):
            left_size = k - len(top_k)

            if left_size <= 0:
                break

            if bucket[i]:
                top_k += bucket[i][:min(len(bucket[i]), left_size)]

        return top_k
