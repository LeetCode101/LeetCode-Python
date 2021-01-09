class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        chars = set()

        for c in s:
            if c in chars:
                chars.remove(c)
            else:
                chars.add(c)

        return len(chars) <= 1
