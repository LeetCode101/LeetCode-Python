from typing import List, Set


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        memo = [None] * len(s)

        return self._search(s, 0, words, memo)

    def _search(self, s: str, i: int, words: Set[str], memo: List[bool]) \
            -> bool:
        if i == len(s):
            return True

        if memo[i] is not None:
            return memo[i]

        word = ''

        for j in range(i, len(s)):
            word += s[j]

            if word in words and self._search(s, j + 1, words, memo):
                memo[i] = True

                return True

        memo[i] = False

        return False
