import collections
import heapq
from typing import List


class Word:
    def __init__(self, word, frequency):
        self.word = word
        self.frequency = frequency

    def __lt__(self, other):
        if self.frequency == other.frequency:
            return self.word > other.word

        return self.frequency < other.frequency


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequencies = collections.Counter(words)
        heap = []

        for word, frequency in frequencies.items():
            heapq.heappush(heap, Word(word, frequency))

            if len(heap) > k:
                heapq.heappop(heap)

        top_k = []

        for _ in range(k):
            top_k.append(heapq.heappop(heap).word)

        return top_k[::-1]
