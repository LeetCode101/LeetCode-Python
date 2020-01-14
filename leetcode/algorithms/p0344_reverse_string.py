from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        low, high = 0, len(s) - 1

        while low < high:
            s[low], s[high] = s[high], s[low]

            low += 1
            high -= 1
