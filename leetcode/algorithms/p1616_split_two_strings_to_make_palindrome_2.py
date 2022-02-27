class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        return self._check(a, b) or self._check(b, a)

    def _check(self, a, b):
        low, high = 0, len(a) - 1

        while low < high and a[low] == b[high]:
            low += 1
            high -= 1

        return self._is_palindrome(a, low, high) \
            or self._is_palindrome(b, low, high)

    def _is_palindrome(self, s, low, high):
        while low < high:
            if s[low] != s[high]:
                return False

            low += 1
            high -= 1

        return True
