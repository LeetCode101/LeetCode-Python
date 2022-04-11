from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []

        self._search(s, 0, '', result)

        return result

    def _search(self, s, start, permutation, result):
        if len(permutation) == len(s):
            result.append(permutation)

        if start == len(s):
            return

        c = s[start]

        self._search(s, start + 1, permutation + c, result)

        if c.isalpha():
            if c.isupper():
                self._search(s, start + 1, permutation + c.lower(), result)
            elif c.islower():
                self._search(s, start + 1, permutation + c.upper(), result)
