import collections
from typing import List


class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str],
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

            if word1 == word2 or word1 in similarities[word2] \
                    or word2 in similarities[word1]:
                continue
            else:
                return False

        return True
