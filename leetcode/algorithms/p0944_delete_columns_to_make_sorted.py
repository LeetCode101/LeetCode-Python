from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if not strs:
            return 0

        count = 0

        for i in range(len(strs[0])):
            j = 1

            while j < len(strs) and strs[j][i] >= strs[j - 1][i]:
                j += 1

            if j != len(strs):
                count += 1

        return count
