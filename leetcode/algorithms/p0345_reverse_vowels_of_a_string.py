class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [i for i, c in enumerate(s) if c
                  in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']]
        low, high = 0, len(vowels) - 1
        chars = list(s)

        while low < high:
            chars[vowels[low]], chars[vowels[high]] = \
                chars[vowels[high]], chars[vowels[low]]
            low += 1
            high -= 1

        return ''.join(chars)
