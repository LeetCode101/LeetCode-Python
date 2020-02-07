class Solution:
    def titleToNumber(self, s: str) -> int:
        letters = dict(zip([chr(x) for x in range(65, 91)],
                           [x for x in range(1, 27)]))
        number = 0

        for c in s:
            number *= 26
            number += letters[c]

        return number
