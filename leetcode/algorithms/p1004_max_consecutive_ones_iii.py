from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        zeros = 0
        max_length = 0
        window_start = 0

        for j in range(len(A)):
            if A[j] == 0:
                zeros += 1

            while zeros > K:
                if A[window_start] == 0:
                    zeros -= 1

                window_start += 1

            max_length = max(max_length, j - window_start + 1)

        return max_length
