from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orders = [-1] * 26

        for i, c in enumerate(order):
            orders[ord(c) - 97] = i

        for i in range(1, len(words)):
            word1 = words[i - 1]
            word2 = words[i]

            if not self._is_smaller(word1, word2, orders):
                return False

        return True

    def _is_smaller(self, word1, word2, orders):
        j = k = 0

        while j < len(word1) and k < len(word2):
            order1 = orders[ord(word1[j]) - 97]
            order2 = orders[ord(word2[k]) - 97]

            if order1 < order2:
                return True
            elif order1 > order2:
                return False
            else:
                j += 1
                k += 1

        return len(word1) <= len(word2)
