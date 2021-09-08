import sys
from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [-sys.maxsize] + arr + [-sys.maxsize]
        n = len(arr)
        stack = []
        result = 0
        mod = pow(10, 9) + 7

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                index = stack.pop()
                result += arr[index] * (index - stack[-1]) * (i - index) % mod
                result %= mod

            stack.append(i)

        return result
