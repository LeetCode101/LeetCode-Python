from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if not nums1 or not nums2:
            return 0

        m, n = len(nums1), len(nums2)
        max_length = 0
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1 if i >= 1 and j >= 1 else 1
                    max_length = max(max_length, dp[i][j])

        return max_length
