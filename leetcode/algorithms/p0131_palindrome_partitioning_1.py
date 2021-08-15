from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        self._search(s, 0, [], result)

        return result

    def _search(self, s, start, partition, result):
        if start == len(s) and partition:
            result.append(partition)

            return

        for end in range(start, len(s)):
            if not self._is_palindrome(s, start, end):
                continue

            self._search(s, end + 1, partition + [s[start:end + 1]], result)

    def _is_palindrome(self, s, low, high):
        while low < high and s[low] == s[high]:
            low += 1
            high -= 1

        return low >= high
