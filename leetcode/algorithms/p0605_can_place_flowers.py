from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers = flowerbed[:]
        i = 0
        length = len(flowerbed)

        while i < length and n > 0:
            flower = flowers[i]
            left_ok = i - 1 < 0 or \
                (i - 1 >= 0 and flowers[i - 1] == 0)
            right_ok = i + 1 == length or \
                (i + 1 < length and flowers[i + 1] == 0)

            if flower != 1 and left_ok and right_ok:
                n -= 1
                flowers[i] = 1

            i += 1

        return n == 0
