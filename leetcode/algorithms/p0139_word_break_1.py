# Time Limit Exceeded!
from typing import List, Set


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)

        return self.search(s, 0, words)

    def search(self, s: str, i: int, words: Set[str]) -> bool:
        if i == len(s):
            return True

        word = ''

        for j in range(i, len(s)):
            word += s[j]

            if word in words:
                found = self.search(s, j + 1, words)

                if found:
                    return True

        return False
