from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even, odd = 0, 1
        length = len(A)

        while even < length and odd < length:
            while even < length and A[even] & 1 == 0:
                even += 2

            while odd < length and A[odd] & 1 == 1:
                odd += 2

            if even < length and odd < length:
                A[even], A[odd] = A[odd], A[even]
                even += 2
                odd += 2

        return A
