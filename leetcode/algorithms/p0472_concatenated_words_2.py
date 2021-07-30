from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        sorted_words = sorted(words, key=lambda x: len(x))
        word_set = set()
        result = []

        for word in sorted_words:
            dp = [False] * (len(word) + 1)
            dp[0] = True

            for i in range(1, len(word) + 1):
                for j in range(i):
                    if dp[j] and word[j:i] in word_set:
                        dp[i] = True

                        break

            if len(word) > 0 and dp[len(word)]:
                result.append(word)

            word_set.add(word)

        return result
