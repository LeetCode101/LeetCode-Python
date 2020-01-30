class Solution:
    def myAtoi(self, s: str) -> int:
        max_positive = pow(2, 31) - 1
        min_negative = -max_positive - 1
        negative = False
        result = 0
        i, length = 0, len(s)

        while i < length and s[i].isspace():
            i += 1

        if i == length:
            return 0

        if s[i] == '+' or s[i] == '-':
            negative = s[i] == '-'
            i += 1

        while i < length and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        return max(-result, min_negative) if negative \
            else min(result, max_positive)
