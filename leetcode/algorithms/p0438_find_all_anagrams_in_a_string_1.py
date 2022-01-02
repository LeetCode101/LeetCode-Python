from typing import List


# Memory Limit Exceeded!
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        anagrams = set()

        self._get_anagrams(p, len(p), '', anagrams)

        start = 0
        chars_so_far = ''
        positions = []

        for c in s:
            chars_so_far += c

            if len(chars_so_far) < len(p):
                continue
            elif len(chars_so_far) > len(p):
                chars_so_far = chars_so_far[1:]
                start += 1

            if chars_so_far in anagrams:
                positions.append(start)

        return positions

    def _get_anagrams(self, s, n, anagram, anagrams):
        if len(anagram) == n:
            anagrams.add(anagram)

            return

        for i, c in enumerate(s):
            self._get_anagrams(s[0:i] + s[i + 1:], n, anagram + c, anagrams)
