class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        n = len(s)
        i = 0
        substring = {}

        for j in range(n):
            if s[j] in substring:
                index = substring[s[j]]

                for k in range(i, index + 1):
                    del substring[s[k]]

                i = index + 1

            max_length = max(max_length, j - i + 1)
            substring[s[j]] = j

        return max_length
