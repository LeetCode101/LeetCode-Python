from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        zeros = 0
        max_length = 0
        i = 0

        for j in range(len(A)):
            if A[j] == 0:
                zeros += 1

            while zeros > K:
                if A[i] == 0:
                    zeros -= 1

                i += 1

            max_length = max(max_length, j - i + 1)

        return max_length
