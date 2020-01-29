class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        i = 0

        while i < len(s):
            while i < len(s) and s[i] == ' ':
                i += 1

            word = ''

            while i < len(s) and s[i] != ' ':
                word += s[i]
                i += 1

            if word:
                words.append(word)

        low, high = 0, len(words) - 1

        while low < high:
            words[low], words[high] = words[high], words[low]
            low += 1
            high -= 1

        return ' '.join(words)
