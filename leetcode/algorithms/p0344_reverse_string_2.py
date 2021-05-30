from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        self._reverse(s, 0, len(s) - 1)

    def _reverse(self, s, low, high):
        if low >= high:
            return

        s[low], s[high] = s[high], s[low]

        self._reverse(s, low + 1, high - 1)
