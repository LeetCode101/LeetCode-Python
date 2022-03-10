from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        sorted_position = sorted(position)
        left, right = 0, sorted_position[-1] - sorted_position[0]

        while left < right:
            middle = left + (right - left) // 2 + 1
            count = self._count(sorted_position, middle)

            if count >= m:
                left = middle
            else:
                right = middle - 1

        return left

    def _count(self, position, magnetic_force):
        count = 1
        current = position[0]

        for i in range(1, len(position)):
            if position[i] - current >= magnetic_force:
                count += 1
                current = position[i]

        return count
