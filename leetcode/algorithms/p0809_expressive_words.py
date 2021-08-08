from typing import List


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        count = 0

        for word in words:
            i = j = 0

            while i < len(s) and j < len(word):
                if s[i] != word[j]:
                    break

                length1 = 1
                length2 = 1

                while i + 1 < len(s) and s[i] == s[i + 1]:
                    i += 1
                    length1 += 1

                while j + 1 < len(word) and word[j] == word[j + 1]:
                    j += 1
                    length2 += 1

                if (length1 == length2) or \
                        (length1 >= 3 and length2 < length1):
                    i += 1
                    j += 1
                else:
                    break

            if i == len(s) and j == len(word):
                count += 1

        return count
