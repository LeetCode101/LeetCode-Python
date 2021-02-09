from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        tail = 0

        for i in range(len(A)):
            if A[i] & 1 == 0:
                A[tail], A[i] = A[i], A[tail]
                tail += 1

        return A
