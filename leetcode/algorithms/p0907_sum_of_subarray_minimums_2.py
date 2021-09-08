from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr.append(0)
        n = len(arr)
        stack = []
        result = 0
        mod = pow(10, 9) + 7

        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                j = stack.pop()
                prev_index = stack[-1] if stack else -1
                prev_count = j - prev_index - 1
                next_count = i - j - 1
                result += arr[j] * (prev_count + 1) * (next_count + 1) % mod
                result %= mod

            stack.append(i)

        return result
