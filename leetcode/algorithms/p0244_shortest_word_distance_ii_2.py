import collections
from typing import List


class WordDistance:
    def __init__(self, wordsDict: List[str]):
        self.length = len(wordsDict)
        self.positions = collections.defaultdict(list)

        for i, word in enumerate(wordsDict):
            self.positions[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        position1 = self.positions[word1]
        position2 = self.positions[word2]
        i, j = 0, 0
        min_distance = self.length

        while i < len(position1) and j < len(position2):
            min_distance = min(min_distance, abs(position1[i] - position2[j]))

            if position1[i] < position2[j]:
                i += 1
            else:
                j += 1

        return min_distance
