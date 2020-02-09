class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        n = len(s)
        i, j = 0, 0
        substring = set()

        while i < n and j < n:
            if s[j] not in substring:
                substring.add(s[j])
                max_length = max(max_length, j - i + 1)
                j += 1
            else:
                substring.remove(s[i])
                i += 1

        return max_length
