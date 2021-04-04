from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orders = [-1] * 26

        for i, c in enumerate(order):
            orders[ord(c) - 97] = i

        for i in range(1, len(words)):
            word1 = words[i - 1]
            word2 = words[i]
            j = k = 0

            while j < len(word1) and k < len(word2):
                order1 = orders[ord(word1[j]) - 97]
                order2 = orders[ord(word2[k]) - 97]

                if order1 == order2:
                    j += 1
                    k += 1

                    continue
                elif order1 < order2:
                    break
                else:
                    return False

            if j == min(len(word1), len(word2)) and len(word1) > len(word2):
                return False

        return True
