from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        mapping = {}

        for s in strings:
            key = ()

            for i in range(len(s) - 1):
                diff = ord(s[i + 1]) - ord(s[i])
                key += (diff % 26,)

            mapping[key] = mapping.get(key, []) + [s]

        return list(mapping.values())
