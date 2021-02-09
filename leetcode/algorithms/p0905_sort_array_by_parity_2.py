from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        low, high = 0, len(A) - 1

        while low < high:
            while low < len(A) and A[low] & 1 == 0:
                low += 1

            while high >= 0 and A[high] & 1 == 1:
                high -= 1

            if low < high:
                A[low], A[high] = A[high], A[low]
                low += 1
                high -= 1

        return A
