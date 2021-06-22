class Solution:
    def validPalindrome(self, s: str) -> bool:
        low, high = 0, len(s) - 1

        while low < high:
            if s[low] != s[high]:
                return self._is_palindrome(s, low + 1, high) \
                       or self._is_palindrome(s, low, high - 1)
            else:
                low += 1
                high -= 1

        return True

    def _is_palindrome(self, s, low, high):
        while low < high:
            if s[low] != s[high]:
                return False
            else:
                low += 1
                high -= 1

        return True
