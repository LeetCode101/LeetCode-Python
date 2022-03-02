from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        for word in sorted(dictionary, key=lambda x: (-len(x), x)):
            j = 0
            n = len(word)

            for i, c in enumerate(s):
                if c == word[j]:
                    j += 1

                if j == n:
                    return word

        return ''
