class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        current_length = 0

        for c in S:
            if c.isdigit():
                current_length *= int(c)
            else:
                current_length += 1

        for i in range(len(S) - 1, -1, -1):
            c = S[i]

            if c.isdigit():
                current_length //= int(c)
                K %= current_length
            else:
                if K == 0 or K == current_length:
                    return c

                current_length -= 1
