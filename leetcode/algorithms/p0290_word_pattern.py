class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split(' ')
        pattern_to_word = {}
        word_to_pattern = {}

        if len(pattern) != len(words):
            return False

        for i, c in enumerate(pattern):
            if c not in pattern_to_word and words[i] not in word_to_pattern:
                pattern_to_word[c] = words[i]
                word_to_pattern[words[i]] = c
            elif (c in pattern_to_word and pattern_to_word[c] != words[i]) \
                    or (words[i] in word_to_pattern
                        and word_to_pattern[words[i]] != c):
                return False

        return True
