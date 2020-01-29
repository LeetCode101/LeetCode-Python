from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        length = 0
        i, j = 0, 0

        while i < len(chars):
            while j < len(chars) and chars[i] == chars[j]:
                j += 1

            chars[length] = chars[i]
            length += 1

            if j - i > 1:
                for c in str(j - i):
                    chars[length] = c
                    length += 1

            i = j

        return length
