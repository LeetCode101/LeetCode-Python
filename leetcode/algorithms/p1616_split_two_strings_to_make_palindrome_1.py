# Time Limit Exceeded!
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        n = len(a)

        for i in range(n):
            a_prefix, a_suffix = a[:i], a[i:]
            b_prefix, b_suffix = b[:i], b[i:]

            if self._is_palindrome(a_prefix + b_suffix) \
                    or self._is_palindrome(b_prefix + a_suffix):
                return True

        return False

    def _is_palindrome(self, s):
        low, high = 0, len(s) - 1

        while low < high:
            if s[low] != s[high]:
                return False

            low += 1
            high -= 1

        return True
