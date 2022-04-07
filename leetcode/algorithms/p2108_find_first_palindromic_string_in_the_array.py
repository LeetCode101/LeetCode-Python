from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self._is_palindrome(word):
                return word

        return ''

    def _is_palindrome(self, word):
        low, high = 0, len(word) - 1

        while low < high:
            if word[low] != word[high]:
                return False

            low += 1
            high -= 1

        return True
