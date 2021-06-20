class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        result = ''
        i, j = len(num1) - 1, len(num2) - 1

        while i >= 0 or j >= 0:
            current_sum = carry

            if i >= 0:
                current_sum += int(num1[i])
                i -= 1

            if j >= 0:
                current_sum += int(num2[j])
                j -= 1

            carry = current_sum // 10
            result = str(current_sum % 10) + result

        return result if carry == 0 else '1' + result
