import collections
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        start, end, n = 0, 0, len(s)
        positions = []
        counter = collections.Counter(p)

        while end < n:
            c = s[end]

            if counter[c] > 0:
                counter[c] -= 1

                if end - start + 1 == len(p):
                    positions.append(start)

                end += 1
            elif start == end:
                start += 1
                end += 1
            else:
                counter[s[start]] += 1
                start += 1

        return positions
