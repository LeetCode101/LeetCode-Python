class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        carry = 0
        m, n = len(a) - 1, len(b) - 1

        while m >= 0 or n >= 0:
            current_sum = carry + (int(a[m]) if m >= 0 else 0) \
                          + (int(b[n]) if n >= 0 else 0)
            carry = current_sum // 2
            result = str(current_sum % 2) + result
            m -= 1
            n -= 1

        return result if carry == 0 else '1' + result
