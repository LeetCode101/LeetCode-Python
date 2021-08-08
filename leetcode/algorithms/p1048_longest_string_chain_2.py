from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        sorted_words = sorted(words, key=lambda x: len(x))
        max_length = 1
        dp = {}

        for word in sorted_words:
            dp[word] = 1

            for i in range(len(word)):
                prev = word[:i] + word[i + 1:]

                if prev in dp:
                    dp[word] = max(dp[prev] + 1, dp[word])
                    max_length = max(max_length, dp[word])

        return max_length
