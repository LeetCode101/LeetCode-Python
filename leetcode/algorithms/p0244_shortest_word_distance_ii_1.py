import sys
from typing import List


class WordDistance:
    def __init__(self, wordsDict: List[str]):
        self.words = wordsDict

    def shortest(self, word1: str, word2: str) -> int:
        prev_index = -1
        min_distance = sys.maxsize

        for i, word in enumerate(self.words):
            if word != word1 and word != word2:
                continue

            if prev_index != -1 and self.words[prev_index] != word:
                min_distance = min(min_distance, i - prev_index)

            prev_index = i

        return min_distance
