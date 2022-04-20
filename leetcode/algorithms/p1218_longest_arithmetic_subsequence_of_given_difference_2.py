import collections
from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        longest = 0
        dp = collections.defaultdict(int)

        for i in range(n):
            dp[arr[i]] = 1 + dp[arr[i] - difference]
            longest = max(longest, dp[arr[i]])

        return longest
