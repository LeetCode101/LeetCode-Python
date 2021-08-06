from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        word_set = set(words)

        for word in words:
            for i in range(1, len(word)):
                word_set.discard(word[i:])

        return sum(len(word) + 1 for word in word_set)
