class Solution:
    def minimumLength(self, s: str) -> int:
        low, high = 0, len(s) - 1

        while low <= high:
            if s[low] != s[high] or low == high:
                return high - low + 1

            i, j = low, high

            while i < high and s[i] == s[low]:
                i += 1

            while j > low and s[j] == s[high]:
                j -= 1

            if i <= j and s[i] != s[low]:
                low = i
                high = j
            else:
                return 0

        return 0
