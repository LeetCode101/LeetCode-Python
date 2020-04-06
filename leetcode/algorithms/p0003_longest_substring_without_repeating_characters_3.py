class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        n = len(s)
        i = 0
        substring = {}

        for j in range(n):
            if s[j] in substring:
                i = max(substring[s[j]] + 1, i)

            max_length = max(max_length, j - i + 1)
            substring[s[j]] = j

        return max_length
