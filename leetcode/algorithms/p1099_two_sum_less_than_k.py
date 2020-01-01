from typing import List


class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()

        max_sum = -1
        i, j = 0, len(A) - 1

        while i < j:
            current_sum = A[i] + A[j]

            if current_sum >= K:
                j -= 1
            else:
                i += 1
                max_sum = max(max_sum, current_sum)

        return max_sum
