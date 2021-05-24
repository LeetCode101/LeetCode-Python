class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        decoded = ''
        digit = 0
        i = 0
        index_before_digit = -1

        while i < len(abbr):
            if abbr[i].isdigit():
                if int(abbr[i]) == 0:
                    return False

                while i < len(abbr) and abbr[i].isdigit():
                    digit = 10 * digit + int(abbr[i])
                    i += 1

                start = index_before_digit + 1
                end = start + digit

                if end > len(word):
                    return False

                decoded += word[start:end]
                index_before_digit = len(decoded) - 1
                digit = 0
            else:
                decoded += abbr[i]
                index_before_digit += 1
                i += 1

        return word == decoded
