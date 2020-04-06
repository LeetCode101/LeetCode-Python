class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        max_length = 0
        substring = {}

        for j, c in enumerate(s):
            if c in substring:
                i = max(substring[c] + 1, i)

            max_length = max(max_length, j - i + 1)
            substring[c] = j

        return max_length
