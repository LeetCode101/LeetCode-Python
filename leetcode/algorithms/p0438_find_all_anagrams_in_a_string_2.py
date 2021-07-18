import collections
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        start = 0
        positions = []
        counter = collections.Counter(p)
        current_counter = collections.defaultdict(int)

        for end, c in enumerate(s):
            current_counter[c] += 1
            current_length = end - start + 1

            if current_length < len(p):
                continue
            elif current_length > len(p):
                current_counter[s[start]] -= 1

                if current_counter[s[start]] == 0:
                    current_counter.pop(s[start])

                start += 1

            if current_counter == counter:
                positions.append(start)

        return positions
