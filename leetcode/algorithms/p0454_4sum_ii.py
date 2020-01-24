from typing import List


class Solution:
    def fourSumCount(
            self, A: List[int], B: List[int], C: List[int], D: List[int]) \
            -> int:
        count = 0
        length = len(A)
        mapping1, mapping2 = {}, {}

        for i in range(length):
            for j in range(length):
                sum1 = A[i] + B[j]
                sum2 = C[i] + D[j]

                if sum1 in mapping1:
                    mapping1[sum1] = mapping1[sum1] + 1
                else:
                    mapping1[sum1] = 1

                if sum2 in mapping2:
                    mapping2[sum2] = mapping2[sum2] + 1
                else:
                    mapping2[sum2] = 1

        for key, value in mapping1.items():
            count += value * mapping2.get(-key, 0)

        return count
