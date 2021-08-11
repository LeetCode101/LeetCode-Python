class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        i = j = 0

        while i < len(s) and j < len(t):
            while i < len(s) and j < len(t) and s[i] == t[j]:
                i += 1
                j += 1

            while i < len(s) and j < len(t) and s[i] != t[j]:
                j += 1

        return i == len(s)
