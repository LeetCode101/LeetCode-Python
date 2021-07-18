from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        sorted_words = sorted(words)
        current_words = []
        word_length = len(words[0])
        start = 0
        positions = []

        for end in range(len(words) * word_length - 1, len(s)):
            for i in range(len(words)):
                word_start, word_end = start + i * word_length, \
                                       start + (i + 1) * word_length
                word = s[word_start:word_end]
                current_words.append(word)

            if sorted(current_words) == sorted_words:
                positions.append(start)

            start += 1
            current_words = []

        return positions
