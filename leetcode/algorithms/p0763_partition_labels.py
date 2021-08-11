from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        rightmost = {c: i for i, c in enumerate(s)}
        left, right = 0, 0
        result = []

        for i, c in enumerate(s):
            right = max(right, rightmost[c])

            if i == right:
                result.append(right - left + 1)
                left = i + 1

        return result
