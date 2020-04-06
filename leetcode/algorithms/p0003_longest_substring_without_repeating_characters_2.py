class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        max_length = 0
        substring = {}

        for j, c in enumerate(s):
            if c in substring:
                index = substring[c]

                for k in range(i, index + 1):
                    del substring[s[k]]

                i = index + 1

            max_length = max(max_length, j - i + 1)
            substring[c] = j

        return max_length
