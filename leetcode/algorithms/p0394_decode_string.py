class Solution:
    def decodeString(self, s: str) -> str:
        result = ''
        digit = 0
        i, length = 0, len(s)

        while i < length:
            c = s[i]

            if c.isdigit():
                digit = digit * 10 + int(c)
            elif c == '[':
                j = i + 1
                brackets = 1

                while j < length:
                    if s[j] == '[':
                        brackets += 1

                    if s[j] == ']':
                        brackets -= 1

                    if brackets == 0:
                        break

                    j += 1

                result += self.decodeString(s[i + 1:j]) * digit
                i = j
                digit = 0
            else:
                result += c

            i += 1

        return result
