class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        i, n = 0, len(num)

        while i < n:
            while stack and stack[-1] > num[i] and k > 0:
                stack.pop()
                k -= 1

            stack.append(num[i])
            i += 1

        for _ in range(k):
            stack.pop()

        i = 0

        while i < len(stack) and stack[i] == '0':
            i += 1

        return ''.join(stack[i:]) or '0'
