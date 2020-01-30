class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        start, end = 0, 0
        i = 0

        while i < length:
            left, right = i, i

            while right < length - 1 and s[right] == s[right + 1]:
                right += 1

            i = right + 1

            while right < length - 1 and left > 0 \
                    and s[right + 1] == s[left - 1]:
                left -= 1
                right += 1

            if right - left > end - start:
                start, end = left, right

        return s[start:end + 1]
