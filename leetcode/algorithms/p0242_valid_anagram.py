class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_mapping = {}

        for c in s:
            if c in char_mapping:
                char_mapping[c] = char_mapping[c] + 1
            else:
                char_mapping[c] = 1

        for c in t:
            if c not in char_mapping:
                return False
            elif char_mapping[c] > 1:
                char_mapping[c] = char_mapping[c] - 1
            else:
                char_mapping.pop(c)

        return len(char_mapping) == 0
