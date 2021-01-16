from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        numbers = set()

        for n in arr:
            if n * 2 in numbers or n / 2 in numbers:
                return True

            numbers.add(n)

        return False
