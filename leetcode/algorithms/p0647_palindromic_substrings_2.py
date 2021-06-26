class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        for i in range(n):
            count += self._count_palindrome(s, i, i, n)
            count += self._count_palindrome(s, i, i + 1, n)

        return count

    def _count_palindrome(self, s, low, high, n):
        count = 0

        while low >= 0 and high < n and s[low] == s[high]:
            low -= 1
            high += 1
            count += 1

        return count
