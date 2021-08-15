from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        cache = {}

        self._search(s, 0, [], result, cache)

        return result

    def _search(self, s, start, partition, result, cache):
        if start == len(s) and partition:
            result.append(partition)

            return

        for end in range(start, len(s)):
            is_cached, palindrome = cache.get((start, end), (False, ''))

            if is_cached and palindrome:
                self._search(s, end + 1, partition + [s[start:end + 1]],
                             result, cache)
            elif not is_cached:
                is_palindrome = self._is_palindrome(s, start, end)
                palindrome = s[start:end + 1] if is_palindrome else ''
                cache[(start, end)] = (True, palindrome)

                if is_palindrome:
                    self._search(s, end + 1, partition + [palindrome],
                                 result, cache)

    def _is_palindrome(self, s, low, high):
        while low < high and s[low] == s[high]:
            low += 1
            high -= 1

        return low >= high
