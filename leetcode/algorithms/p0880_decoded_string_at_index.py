# OverflowError!
class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        return self._decode_string(S)[K - 1]

    def _decode_string(self, s: str) -> str:
        text = ''
        digit = 0

        for i, c in enumerate(s):
            if c.isdigit():
                digit = digit * 10 + int(c)

                if i == len(s) - 1:
                    text *= digit
            else:
                if digit > 0:
                    text *= digit
                    digit = 0

                text += c

        return text
