from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        sorted_words = sorted(words, key=lambda x: len(x))
        n = len(words)
        dp = [1] * n

        for i in range(1, n):
            j = i - 1
            word_length = len(sorted_words[i])
            max_length = 1

            while j >= 0 and len(sorted_words[j]) == word_length:
                j -= 1

            while j >= 0 and len(sorted_words[j]) + 1 == word_length:
                if self._is_valid(sorted_words[j], sorted_words[i]):
                    max_length = max(max_length, dp[j] + 1)

                j -= 1

            dp[i] = max_length

        return max(dp)

    def _is_valid(self, word1, word2):
        i, j = 0, 0

        while i < len(word1) and j < len(word2) and word1[i] == word2[j]:
            i += 1
            j += 1

        j += 1

        while i < len(word1) and j < len(word2) and word1[i] == word2[j]:
            i += 1
            j += 1

        return i == len(word1) and j == len(word2)
