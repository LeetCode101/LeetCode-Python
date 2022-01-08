import collections
import string
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) \
            -> List[List[str]]:
        words = set(wordList)
        result = []
        layer = {beginWord: [[beginWord]]}
        letters = string.ascii_lowercase

        while layer:
            new_layer = collections.defaultdict(list)

            for word in layer:
                if word == endWord:
                    result.extend([x for x in layer[word]])
                else:
                    for i in range(len(word)):
                        for c in letters:
                            new_word = word[:i] + c + word[i + 1:]

                            if new_word in words:
                                new_layer[new_word] += \
                                    [x + [new_word] for x in layer[word]]

            words -= set(new_layer.keys())
            layer = new_layer

        return result
