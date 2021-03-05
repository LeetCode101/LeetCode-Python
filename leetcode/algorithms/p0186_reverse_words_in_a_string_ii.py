from typing import List


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        self._reverse(s, 0, len(s) - 1)

        start, end = 0, 0

        while end < len(s):
            while start < len(s) and s[start].isspace():
                start += 1
                end += 1

            while end < len(s) and not s[end].isspace():
                end += 1

            self._reverse(s, start, end - 1)

            start = end

    def _reverse(self, s: List[str], low: int, high: int) -> None:
        while low < high:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1
