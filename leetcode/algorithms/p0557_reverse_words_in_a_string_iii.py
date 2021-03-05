from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        n = len(s)
        words = ''

        while i < n:
            if s[i].isspace():
                words += ' '
                i += 1
                continue

            word = []

            while i < n and not s[i].isspace():
                word.append(s[i])
                i += 1

            words += ''.join(self._reverse_word(word))

        return words

    def _reverse_word(self, s: List[str]):
        low, high = 0, len(s) - 1

        while low < high:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1

        return s
