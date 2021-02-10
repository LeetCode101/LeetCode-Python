import collections


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counts = collections.Counter(s)
        found_odd_count = False

        for key, value in counts.items():
            if value & 1 == 1:
                if found_odd_count:
                    return False
                else:
                    found_odd_count = True

        return True
