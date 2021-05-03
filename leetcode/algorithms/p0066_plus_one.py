from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return []

        carry = 1
        new_digits = [0] * len(digits)

        for i in range(len(digits) - 1, -1, -1):
            current_sum = digits[i] + carry
            carry = current_sum // 10
            new_digits[i] = current_sum % 10

        return new_digits if carry == 0 else [carry] + new_digits
