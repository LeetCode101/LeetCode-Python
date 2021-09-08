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
                index = stack.pop()
                prev_index = stack[-1] if stack else -1
                prev_count = index - prev_index - 1
                next_count = i - index - 1
                result += arr[index] * (prev_count + 1) * (next_count + 1) % mod
                result %= mod

            stack.append(i)

        return result
