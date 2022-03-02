from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        longest = ''

        for word in dictionary:
            j = 0
            n = len(word)

            for i, c in enumerate(s):
                if c == word[j]:
                    j += 1

                if j == n:
                    if len(word) > len(longest):
                        longest = word
                    elif len(word) == len(longest) and word < longest:
                        longest = word

                    break

        return longest
