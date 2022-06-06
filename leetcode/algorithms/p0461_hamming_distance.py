class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0

        while x > 0 and y > 0:
            a = x & 1
            b = y & 1
            x = x >> 1
            y = y >> 1

            if a != b:
                count += 1

        if x > 0:
            count += self._count_one(x)

        if y > 0:
            count += self._count_one(y)

        return count

    def _count_one(self, x):
        count = 0

        while x > 0:
            if x & 1:
                count += 1

            x = x >> 1

        return count
