from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        m = len(s)
        longest = ''

        for word in dictionary:
            i, j = 0, 0
            n = len(word)

            while i < m and j < n:
                if s[i] == word[j]:
                    j += 1

                i += 1

                if j == n:
                    break

            if j == n:
                if len(word) > len(longest):
                    longest = word
                elif len(word) == len(longest) and word < longest:
                    longest = word

        return longest
