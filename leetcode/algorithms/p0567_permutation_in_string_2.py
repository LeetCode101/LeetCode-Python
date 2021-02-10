import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = collections.Counter(s1)
        counts2 = {}

        for i, c in enumerate(s2):
            counts2[c] = counts2.get(c, 0) + 1

            if i >= len(s1):
                removed = s2[i - len(s1)]
                counts2[removed] -= 1

                if counts2[removed] == 0:
                    del counts2[removed]

            if counts1 == counts2:
                return True

        return False
