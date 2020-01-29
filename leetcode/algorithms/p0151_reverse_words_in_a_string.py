class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        i, j = 0, 0

        while i < len(s):
            while i < len(s) and s[i] == ' ' and s[j] == ' ':
                i += 1
                j += 1

            word = ''

            while j < len(s) and s[j] != ' ':
                word += s[j]
                j += 1

            if word:
                words.append(word)

            i = j

        low, high = 0, len(words) - 1

        while low < high:
            words[low], words[high] = words[high], words[low]
            low += 1
            high -= 1

        return ' '.join(words)
