class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        i, n = 0, len(haystack)

        while i < n:
            if i + len(needle) > n:
                break

            while i < n and haystack[i] != needle[0]:
                i += 1

            j, k = i, 0

            while j < n and k < len(needle) and haystack[j] == needle[k]:
                j += 1
                k += 1

            if k == len(needle):
                return i

            i += 1

        return -1
