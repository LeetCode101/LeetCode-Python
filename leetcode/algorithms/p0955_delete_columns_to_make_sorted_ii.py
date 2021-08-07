from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n = len(strs), len(strs[0])
        count = 0
        in_order = [False] * (m - 1)

        for i in range(n):
            removed = False
            current_in_order = in_order[:]

            for j in range(m - 1):
                if not in_order[j] and strs[j][i] > strs[j + 1][i]:
                    count += 1
                    removed = True

                    break
                elif strs[j][i] < strs[j + 1][i] and not in_order[j]:
                    current_in_order[j] = True

            if not removed:
                in_order = current_in_order

        return count
