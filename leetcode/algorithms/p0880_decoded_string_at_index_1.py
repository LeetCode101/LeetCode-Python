# Time Limit Exceeded!
class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        return self._decode_string(S)[K - 1]

    def _decode_string(self, s: str) -> str:
        text = ''

        for i, c in enumerate(s):
            if c.isdigit():
                text *= int(c)
            else:
                text += c

        return text
