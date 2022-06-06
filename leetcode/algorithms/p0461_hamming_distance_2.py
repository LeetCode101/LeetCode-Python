class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return self._count_one(x ^ y)

    def _count_one(self, x):
        count = 0

        while x > 0:
            if x & 1:
                count += 1

            x = x >> 1

        return count
