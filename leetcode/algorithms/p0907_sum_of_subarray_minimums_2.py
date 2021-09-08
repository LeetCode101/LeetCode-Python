from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        result = 0
        left = [0] * n
        right = [0] * n
        stack = []
        mod = pow(10, 9) + 7

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            right[i] = stack[-1] if stack else n
            stack.append(i)

        for i in range(n):
            result += (i - left[i]) * (right[i] - i) * arr[i]
            result %= mod

        return result
