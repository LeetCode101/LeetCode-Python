class Solution:
    def myAtoi(self, s: str) -> int:
        max_positive = pow(2, 31) - 1
        min_negative = -max_positive - 1

        sign = ''
        i, length = 0, len(s)

        while i < length and s[i].isspace():
            i += 1

        if i == length:
            return 0

        if s[i] == '+' or s[i] == '-':
            sign = s[i]
            i += 1

        result = 0

        while i < length and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        return max(-result, min_negative) if sign == '-' \
            else min(result, max_positive)
