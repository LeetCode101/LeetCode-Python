from typing import List


class Solution:
    def expand(self, s: str) -> List[str]:
        result = []

        self._search(s, 0, '', result)

        return sorted(result)

    def _search(self, s, start, permutation, result):
        if start == len(s):
            result.append(permutation)

            return

        c = s[start]

        if c.isalpha():
            self._search(s, start + 1, permutation + c, result)
        else:
            j = start + 1
            chars = []

            while s[j] != '}':
                if s[j].isalpha():
                    chars.append(s[j])

                j += 1

            for x in chars:
                self._search(s, j + 1, permutation + x, result)
