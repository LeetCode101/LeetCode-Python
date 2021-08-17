from typing import List


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        stones = sorted([a, b, c])
        a, b, c = stones

        if b - a == c - b == 1:
            return [0, 0]
        else:
            return [1 if min(b - a, c - b) <= 2 else 2, c - a - 2]
