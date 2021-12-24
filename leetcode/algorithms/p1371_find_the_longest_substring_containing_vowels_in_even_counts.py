class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {
            'a': 0,
            'e': 1,
            'i': 2,
            'o': 3,
            'u': 4
        }
        positions = {0: -1}
        max_length = 0
        mask = 0

        for i, c in enumerate(s):
            if c in vowels:
                mask ^= 1 << vowels[c]

            if mask not in positions:
                positions[mask] = i
            else:
                max_length = max(max_length, i - positions[mask])

        return max_length
