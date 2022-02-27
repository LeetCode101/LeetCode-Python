class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        return self._check(a, b) or self._check(b, a)

    def _check(self, a, b):
        low, high = 0, len(a) - 1

        while low < high and a[low] == b[high]:
            low += 1
            high -= 1

        return self._has_palindrome(a, low, high) \
               or self._has_palindrome(b, low, high)

    def _has_palindrome(self, s, low, high):
        while low < high and s[low] == s[high]:
            low += 1
            high -= 1

        return low >= high
