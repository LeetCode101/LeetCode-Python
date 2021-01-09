class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counts = {}
        found_odd_count = False

        for c in s:
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1

        for key, value in counts.items():
            if value & 1 == 1:
                if found_odd_count:
                    return False
                else:
                    found_odd_count = True

        return True
