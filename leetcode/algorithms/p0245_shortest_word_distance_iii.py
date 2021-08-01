import sys
from typing import List


class Solution:
    def shortestWordDistance(self, wordsDict: List[str],
                             word1: str, word2: str) -> int:
        prev_index = -1
        min_distance = sys.maxsize

        for i, word in enumerate(wordsDict):
            if word != word1 and word != word2:
                continue

            if prev_index != -1 and \
                    (wordsDict[prev_index] != word or word1 == word2):
                min_distance = min(min_distance, i - prev_index)

            prev_index = i

        return min_distance
