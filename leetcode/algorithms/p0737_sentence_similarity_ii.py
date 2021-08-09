import collections
from typing import List


class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str],
                               sentence2: List[str],
                               similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        similarities = collections.defaultdict(set)

        for a, b in similarPairs:
            similarities[a].add(b)
            similarities[b].add(a)

        for i in range(len(sentence1)):
            word1 = sentence1[i]
            word2 = sentence2[i]

            if word1 == word2 or self._is_similar(
                    word1, word2, similarities, collections.defaultdict(bool)):
                continue
            else:
                return False

        return True

    def _is_similar(self, word1, word2, similarities, visited):
        if (word1, word2) in visited:
            return visited[(word1, word2)]

        if word1 in similarities[word2]:
            visited[(word1, word2)] = True

            return True
        else:
            visited[(word1, word2)] = False

        for word in similarities[word1]:
            if self._is_similar(word, word2, similarities, visited):
                return True

        return False
