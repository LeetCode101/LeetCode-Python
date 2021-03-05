import collections
from typing import List


# Time Limit Exceeded!
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []

        anagrams = {
            strs[0]: [strs[0]]
        }

        for i in range(1, len(strs)):
            found = False

            for key, value in anagrams.items():
                if self._is_anagram(key, strs[i]):
                    anagrams[key].append(strs[i])

                    found = True

            if not found:
                anagrams[strs[i]] = [strs[i]]

        return list(anagrams.values())

    def _is_anagram(self, a: str, b: str) -> bool:
        chars = collections.Counter(a)

        for c in b:
            if c not in chars:
                return False
            elif chars[c] == 1:
                chars.pop(c)
            else:
                chars[c] -= 1

        return len(chars) == 0
