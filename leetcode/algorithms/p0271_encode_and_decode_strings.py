class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = ''

        for s in strs:
            encoded += str(len(s)) + '#' + s

        return encoded

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        digit = 0
        i, length = 0, len(s)
        result = []

        while i < length:
            c = s[i]

            if c.isdigit():
                digit = digit * 10 + int(c)
                i += 1
            elif c == '#':
                end = i + 1 + digit
                result.append(s[i + 1:end])
                digit = 0
                i = end

        return result
